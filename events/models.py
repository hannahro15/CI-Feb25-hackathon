# events/models.py
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.validators import URLValidator
from cloudinary.models import CloudinaryField
import cloudinary
import uuid

class EventCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Event Categories"
    
    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey('EventCategory', on_delete=models.PROTECT)
    date = models.DateTimeField()
    duration = models.DurationField()
    location_name = models.CharField(max_length=200)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.PositiveIntegerField()
    spots_remaining = models.PositiveIntegerField()
    booking_url = models.URLField(max_length=500, blank=True, null=True, validators=[URLValidator()])
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_demo = models.BooleanField(default=False)
    image = CloudinaryField(
        'image',
        folder='events',  # This creates an 'events' folder in your Cloudinary account
        null=True,
        blank=True,
        transformation={
            'quality': 'auto:good',
            'fetch_format': 'auto',
            'width': 'auto',
            'crop': 'scale'
        },
        default='default_post_o0lbny'  
    )


    def save(self, *args, **kwargs):
        # Generate a slug if it doesn’t exist
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            count = 1

            # Ensure uniqueness
            while Event.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"
                count += 1

            self.slug = slug

        # Ensure spots_remaining is set correctly
        if not self.spots_remaining:
            self.spots_remaining = self.capacity
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def is_editable_by(self, user):
        """Check if the event can be edited by the given user"""
        return user.is_authenticated and self.created_by == user