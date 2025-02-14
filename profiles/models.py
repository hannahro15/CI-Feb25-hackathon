# profiles/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

def validate_file_size(value):
    filesize = value.size
    if filesize > 1024 * 1024:  # 1MB
        raise ValidationError("Maximum file size is 1MB")

class Interest(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'profiles'  # Explicitly set the app label

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(
        upload_to='profile_images/',
        null=True,
        blank=True,
        validators=[validate_file_size]
    )
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    interests = models.ManyToManyField('profiles.Interest', blank=True)  # Update the reference here
    age_preference = models.CharField(max_length=50, blank=True)
    location_radius = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    class Meta:
        app_label = 'profiles'  # Explicitly set the app label

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()