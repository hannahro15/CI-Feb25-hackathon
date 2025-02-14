from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from profiles.models import UserProfile

class Command(BaseCommand):
    help = 'Creates missing user profiles for existing users'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        
        # Find users without profiles
        users_without_profiles = User.objects.filter(profile__isnull=True)
        
        created_count = 0
        for user in users_without_profiles:
            try:
                # Create profile for users without one
                UserProfile.objects.create(user=user)
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created profile for user: {user.username}')
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Failed to create profile for user {user.username}: {str(e)}')
                )

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {created_count} missing profiles'
            )
        )