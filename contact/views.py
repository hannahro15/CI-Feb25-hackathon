from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def contact(request):
    '''
    Render contact page and form
    '''
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'contact/contact.html', {'form': form})