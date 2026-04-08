from django.shortcuts import render, get_object_or_404
from .models import Flight
from django.db.models import Q

def flight_list(request):
    flights = Flight.objects.all()
    
    # Search parameters
    origin = request.GET.get('origin', '')
    destination = request.GET.get('destination', '')
    date = request.GET.get('date', '')
    cabin_class = request.GET.get('class', '')
    
    if origin:
        flights = flights.filter(origin__icontains=origin)
    if destination:
        flights = flights.filter(destination__icontains=destination)
    if cabin_class:
        flights = flights.filter(cabin_class=cabin_class)
        
    # Get unique airlines and classes for filtering
    airlines = Flight.objects.values_list('airline', flat=True).distinct()
    classes = [c[0] for c in Flight._meta.get_field('cabin_class').choices]
    
    return render(request, 'flights/flight_list.html', {
        'flights': flights,
        'origin': origin,
        'destination': destination,
        'date': date,
        'selected_class': cabin_class,
        'airlines': airlines,
        'classes': classes,
    })

def flight_booking_init(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    # For now, just render a simple placeholder or redirect to a booking form
    return render(request, 'flights/flight_booking.html', {'flight': flight})
