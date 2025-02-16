# Generated by Django 5.1.6 on 2025-02-16 21:52

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_booking_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default='default_profile_ju9xum', max_length=255, null=True, verbose_name='image'),
        ),
    ]
