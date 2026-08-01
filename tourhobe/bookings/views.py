from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from packages.models import Package
from .models import Booking, HotelBooking, FlightBooking
from cabs.models import CabBooking

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
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    hotel_bookings = HotelBooking.objects.filter(user=request.user).order_by('-created_at')
    flight_bookings = FlightBooking.objects.filter(user=request.user).order_by('-created_at')
    cab_bookings = CabBooking.objects.filter(user=request.user).order_by('-created_at')

    total_bookings = bookings.count() + hotel_bookings.count() + flight_bookings.count() + cab_bookings.count()
    
    pending_count = (
        bookings.filter(status="pending").count() + 
        hotel_bookings.filter(status="pending").count() + 
        flight_bookings.filter(status="pending").count() + 
        cab_bookings.filter(status="pending").count()
    )
    
    approved_count = (
        bookings.filter(status="approved").count() + 
        hotel_bookings.filter(status="approved").count() + 
        flight_bookings.filter(status="approved").count() + 
        cab_bookings.filter(status="confirmed").count() # cab uses confirmed
    )

    context = {
        'bookings': bookings,
        'hotel_bookings': hotel_bookings,
        'flight_bookings': flight_bookings,
        'cab_bookings': cab_bookings,
        'total_bookings': total_bookings,
        'pending_count': pending_count,
        'approved_count': approved_count,
    }
    return render(request, 'bookings/my_bookings.html', context)


@login_required
def booking_detail(request, booking_type, booking_id):
    booking = None
    item_title = ""
    item_image_url = ""
    
    if booking_type == 'package':
        booking = get_object_or_404(Booking, id=booking_id, user=request.user)
        item_title = booking.package.title
        if booking.package.image:
            item_image_url = booking.package.image.url
    elif booking_type == 'hotel':
        booking = get_object_or_404(HotelBooking, id=booking_id, user=request.user)
        item_title = booking.hotel.name
        if booking.hotel.image:
            item_image_url = booking.hotel.image.url
    elif booking_type == 'flight':
        booking = get_object_or_404(FlightBooking, id=booking_id, user=request.user)
        item_title = booking.flight.airline
        if booking.flight.logo:
            item_image_url = booking.flight.logo.url
    elif booking_type == 'cab':
        booking = get_object_or_404(CabBooking, id=booking_id, user=request.user)
        item_title = booking.cab.title if booking.cab else "Unknown Cab"
        if booking.cab and booking.cab.primary_image:
            item_image_url = booking.cab.primary_image.url

    context = {
        'booking': booking,
        'booking_type': booking_type,
        'item_title': item_title,
        'item_image_url': item_image_url
    }
    return render(request, 'bookings/booking_detail.html', context)
