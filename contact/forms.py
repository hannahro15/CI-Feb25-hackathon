from django import forms
from .models import ContactForm

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'message']