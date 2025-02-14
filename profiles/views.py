# profiles/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import UserProfile  # Changed from Profile to UserProfile

@login_required
def profile_view(request):
    return render(request, 'profiles/user_profile.html')

@login_required
def profile_edit(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profiles:profile_view')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    
    return render(request, 'profiles/profile_edit.html', context)

@login_required
def upload_avatar(request):
    if request.method == 'POST' and request.FILES.get('avatar'):
        request.user.profile.avatar = request.FILES['avatar']
        request.user.profile.save()
        messages.success(request, 'Profile picture updated successfully!')
    return redirect('profiles:profile_view')