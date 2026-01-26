from django.shortcuts import render, get_object_or_404
from .models import Location, Package, CarouselSlide

def home(request):
    locations = Location.objects.all()
    slides = CarouselSlide.objects.filter(is_active=True)

    return render(request, 'packages/home.html', {
        'locations': locations,
        'slides': slides
    })

def location_packages(request, location_id):
    location = get_object_or_404(Location, id=location_id)
    packages = Package.objects.filter(location=location)

    return render(request, 'packages/location_packages.html', {
        'location': location,
        'packages': packages
    })