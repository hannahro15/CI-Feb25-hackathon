# profiles/signals.py
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Create a UserProfile instance when User instance is created"""
    if created:
        UserProfile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """Ensure profile is saved when user is saved"""
    try:
        # Try to access or create profile if it doesn't exist
        profile, created = UserProfile.objects.get_or_create(user=instance)
        profile.save()
    except Exception as e:
        print(f"Error saving profile: {e}")