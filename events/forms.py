from django import forms
from .models import Event
from django.core.validators import URLValidator


class EventForm(forms.ModelForm):
    # Custom field definitions with placeholder text
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full p-3 rounded-xl border border-gray-200 bg-white/50 focus:outline-none focus:ring-2 focus:ring-rose-500',
            'placeholder': '❤️ Enter a catchy title for your event'
        })
    )
    
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full p-3 rounded-xl border border-gray-200 bg-white/50 focus:outline-none focus:ring-2 focus:ring-rose-500',
            'placeholder': 'Describe your amazing event...',
            'rows': 5
        })
    )
    
    booking_url = forms.URLField(
        required=False,
        validators=[URLValidator()],
        widget=forms.URLInput(attrs={
            'class': 'w-full p-3 rounded-xl border border-gray-200 bg-white/50 focus:outline-none focus:ring-2 focus:ring-rose-500',
            'placeholder': 'https://example.com/book-event'
        })
    )

    image = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'w-full p-3 rounded-xl border border-gray-200 bg-white/50 focus:outline-none focus:ring-2 focus:ring-rose-500',
                'accept': 'image/*'
            }
        )
    )

    class Meta:
        model = Event
        fields = [
            'title',
            'description',
            'category',
            'date',
            'duration',
            'location_name',
            'address',
            'city',
            'state',
            'zip_code',
            'price',
            'capacity',
            'image',
            'booking_url'
        ]
        
        widgets = {
            'date': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'w-full p-3 rounded-xl border border-gray-200 bg-white/50 focus:outline-none focus:ring-2 focus:ring-rose-500'
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'min': '0',
                    'step': '0.01',
                    'class': 'w-full p-3 pl-8 rounded-xl border border-gray-200 bg-white/50 focus:outline-none focus:ring-2 focus:ring-rose-500'
                }
            ),
            'capacity': forms.NumberInput(
                attrs={
                    'min': '1',
                    'class': 'w-full p-3 rounded-xl border border-gray-200 bg-white/50 focus:outline-none focus:ring-2 focus:ring-rose-500'
                }
            )
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Add any image validation you need
            allowed_types = ['image/jpeg', 'image/png', 'image/gif']
            if hasattr(image, 'content_type') and image.content_type not in allowed_types:
                raise forms.ValidationError('Please upload a valid image file (JPEG, PNG, or GIF)')
        return image
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make certain fields optional
        self.fields['image'].required = False
        self.fields['state'].required = False  # Making state optional for international events

        # Add helpful hints
        self.fields['capacity'].help_text = '💝 How many lovely people can attend?'
        self.fields['price'].help_text = '💖 Set a fair price for your event'
        self.fields['booking_url'].help_text = '💓 Add your external booking link (optional)'