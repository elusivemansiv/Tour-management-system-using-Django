from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from packages.models import Package
from .models import Booking

@login_required
def book_package(request, package_id):
    package = get_object_or_404(Package, id=package_id)

    if request.method == 'POST':
        Booking.objects.create(
            user=request.user,
            package=package,
            full_name=request.POST.get('full_name'),
            phone=request.POST.get('phone'),
            travel_date=request.POST.get('travel_date')
        )
        messages.success(request, 'Booking request submitted!')
        return redirect('my_bookings')

    return render(request, 'bookings/book_package.html', {'package': package})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)

    context = {
        'bookings': bookings,
        'total_bookings': bookings.count(),
        'pending_count': bookings.filter(status="Pending").count(),
        'approved_count': bookings.filter(status="Approved").count(),
    }
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})

