from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import RegisterForm, ProfileEditForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from bookings.models import Booking

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'accounts/login.html')


def user_logout(request):
    logout(request)
    return redirect('/')


@login_required
def user_dashboard(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'accounts/dashboard.html', {
        'bookings': bookings
    })

from .forms import RegisterForm, ProfileEditForm, UserProfileForm
from .models import UserProfile

@login_required
def edit_profile(request):
    # Ensure profile exists
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        user_form = ProfileEditForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile_form.save()
            if user_form.cleaned_data.get('new_password'):
                update_session_auth_hash(request, user)
            messages.success(request, 'Profile updated successfully!')
            return redirect('user_dashboard')
    else:
        user_form = ProfileEditForm(instance=request.user)
        profile_form = UserProfileForm(instance=profile)
        
    return render(request, 'accounts/profile.html', {
        'form': user_form,
        'profile_form': profile_form
    })