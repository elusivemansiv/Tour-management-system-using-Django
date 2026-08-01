from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Flight, FlightOffer, PopularDestination
from bookings.models import FlightBooking
from blog.models import BlogPost

def flight_home(request):
    offers = FlightOffer.objects.all()[:4]
    destinations = PopularDestination.objects.all()[:6]
    # Get latest 3 blogs for the blog section
    blogs = BlogPost.objects.order_by('-date_posted')[:3]
    
    return render(request, 'flights/flight_home.html', {
        'offers': offers,
        'destinations': destinations,
        'blogs': blogs,
    })

def flight_list(request):
    flights = Flight.objects.all()
    
    # Search parameters
    origin = request.GET.get('origin', '')
    destination = request.GET.get('destination', '')
    date = request.GET.get('date', '')
    
    if origin:
        flights = flights.filter(origin__icontains=origin)
    if destination:
        flights = flights.filter(destination__icontains=destination)
        
    airlines = Flight.objects.values_list('airline', flat=True).distinct()
    
    return render(request, 'flights/flight_list.html', {
        'flights': flights,
        'origin': origin,
        'destination': destination,
        'date': date,
        'airlines': airlines,
    })

def flight_detail(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    return render(request, 'flights/flight_detail.html', {'flight': flight})

@login_required
def flight_checkout(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    
    if request.method == 'POST':
        FlightBooking.objects.create(
            user=request.user,
            flight=flight,
            full_name=request.POST.get('full_name'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email', request.user.email),
            travel_date=request.POST.get('travel_date'),
            passengers=request.POST.get('passengers', 1),
            fare_class=request.POST.get('fare_class', 'Economy'),
            total_amount=flight.base_price # Simplification
        )
        messages.success(request, 'Flight booking request submitted!')
        return redirect('my_bookings')
        
    return render(request, 'flights/flight_checkout.html', {'flight': flight})
