from django.db import models

# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'