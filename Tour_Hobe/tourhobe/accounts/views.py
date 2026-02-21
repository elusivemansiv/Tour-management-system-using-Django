from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
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