# Generated by Django 4.2 on 2025-02-14 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateTimeField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField(max_length=3)),
                ('bio', models.TextField(max_length=500)),
            ],
        ),
    ]
