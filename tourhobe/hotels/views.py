from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Hotel
from bookings.models import HotelBooking


def hotel_detail(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    rooms = hotel.rooms.all()
    amenities = [a.strip() for a in hotel.amenities.split(',') if a.strip()]

    # Stars as range for template rendering
    stars_filled = range(hotel.star_rating)
    stars_empty = range(5 - hotel.star_rating)

    # Related hotels in the same location (exclude this one)
    related_hotels = Hotel.objects.filter(
        location=hotel.location
    ).exclude(pk=pk)[:3]

    return render(request, 'hotels/hotel_detail.html', {
        'hotel': hotel,
        'rooms': rooms,
        'amenities': amenities,
        'stars_filled': stars_filled,
        'stars_empty': stars_empty,
        'related_hotels': related_hotels,
    })
def hotel_list(request):
    hotels = Hotel.objects.all()
    
    # Filtering
    location_filter = request.GET.get('location')
    tier_filter = request.GET.get('tier')
    star_filter = request.GET.get('star_rating')
    
    if location_filter:
        hotels = hotels.filter(location=location_filter)
    if tier_filter:
        hotels = hotels.filter(tier=tier_filter)
    if star_filter:
        hotels = hotels.filter(star_rating=star_filter)
        
    # Get distinct locations for the filter
    locations = Hotel.objects.values_list('location', flat=True).distinct()
    
    return render(request, 'hotels/hotel_list.html', {
        'hotels': hotels,
        'locations': locations,
        'selected_location': location_filter,
        'selected_tier': tier_filter,
        'selected_star': star_filter,
    })

@login_required
def hotel_checkout(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    
    if request.method == 'POST':
        HotelBooking.objects.create(
            user=request.user,
            hotel=hotel,
            full_name=request.POST.get('full_name'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email', request.user.email),
            check_in=request.POST.get('check_in'),
            check_out=request.POST.get('check_out'),
            guests=request.POST.get('guests', 1),
            total_amount=hotel.price_per_night # Just using base price for now
        )
        messages.success(request, 'Hotel booking request submitted!')
        return redirect('my_bookings')
        
    return render(request, 'hotels/hotel_checkout.html', {'hotel': hotel})
