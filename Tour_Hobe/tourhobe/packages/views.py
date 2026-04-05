from django.shortcuts import render, get_object_or_404
from .models import Location, Package, CarouselSlide
from flights.models import Flight
from hotels.models import Hotel

def home(request):
    locations = Location.objects.all()
    slides = CarouselSlide.objects.filter(is_active=True)
    flights = Flight.objects.all()[:4] # Get top 4 flights
    hotels = Hotel.objects.all()[:4] # Get top 4 hotels

    return render(request, 'packages/home.html', {
        'locations': locations,
        'slides': slides,
        'flights': flights,
        'hotels': hotels,
    })


def location_packages(request, location_id):
    location = get_object_or_404(Location, id=location_id)
    packages = Package.objects.filter(location=location)

    return render(request, 'packages/location_packages.html', {
        'location': location,
        'packages': packages
    })


def package_detail(request, pk):
    package = get_object_or_404(Package, pk=pk)
    return render(request, "packages/package_detail.html", {
        "package": package
    })


def explore(request):
    locations = Location.objects.all()
    return render(request, 'packages/explore.html', {
        'locations': locations
    })


def all_packages(request):
    packages = Package.objects.select_related('location')

    return render(request, 'packages/all_packages.html', {
        'packages': packages
    })

def contact(request):
    return render(request, "packages/contact.html")

def about(request):
    return render(request, "packages/about.html")