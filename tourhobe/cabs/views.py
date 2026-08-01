from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import VehicleType, CabFeature, CabFAQ, Cab, CabBooking
from django.db.models import Q
from datetime import datetime

def cab_home(request):
    vehicle_types = VehicleType.objects.all()
    features = CabFeature.objects.all()
    faqs = CabFAQ.objects.all()
    return render(request, 'cabs/cab_home.html', {
        'vehicle_types': vehicle_types,
        'features': features,
        'faqs': faqs
    })

def cab_list(request):
    cabs = Cab.objects.all()
    
    # Search parameters
    pickup = request.GET.get('pickup', '')
    drop = request.GET.get('drop', '')
    date = request.GET.get('date', '')
    
    if pickup:
        # In a real app we might filter by availability in city, for now just pass to template
        pass
        
    return render(request, 'cabs/cab_list.html', {
        'cabs': cabs,
        'pickup': pickup,
        'drop': drop,
        'date': date
    })

def cab_detail(request, pk):
    cab = get_object_or_404(Cab, pk=pk)
    
    # Passing search params to retain them
    pickup = request.GET.get('pickup', 'San Jacinto, USA')
    drop = request.GET.get('drop', 'North Dakota, Canada')
    date = request.GET.get('date', '23 Jan 2022')
    
    # Basic fare calc based on distance placeholder
    distance_km = 230
    base_price = cab.base_price
    state_tax = 50
    night_charge = 100
    conv_fee = 25
    total = base_price + state_tax + night_charge + conv_fee
    
    return render(request, 'cabs/cab_detail.html', {
        'cab': cab,
        'pickup': pickup,
        'drop': drop,
        'date': date,
        'base_price': base_price,
        'state_tax': state_tax,
        'night_charge': night_charge,
        'conv_fee': conv_fee,
        'total': total,
    })

@login_required
def cab_checkout(request, pk):
    cab = get_object_or_404(Cab, pk=pk)
    if request.method == 'POST':
        # Create booking and render success page
        CabBooking.objects.create(
            user=request.user,
            cab=cab,
            first_name=request.POST.get('first_name', request.user.first_name or request.user.username),
            last_name=request.POST.get('last_name', request.user.last_name),
            email=request.POST.get('email', request.user.email),
            phone=request.POST.get('phone', '0000000000'),
            pickup_city=request.POST.get('pickup', 'Unknown'),
            drop_city=request.POST.get('drop', 'Unknown'),
            pickup_date=request.POST.get('pickup_date') or datetime.now().date(),
            pickup_time=request.POST.get('pickup_time') or datetime.now().time(),
            total_amount=request.POST.get('total_amount', cab.base_price)
        )
        messages.success(request, 'Cab booking request submitted!')
        return redirect('my_bookings')
        
    return render(request, 'cabs/cab_checkout.html', {
        'cab': cab,
    })
