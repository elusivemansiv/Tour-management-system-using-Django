from django.db import models
from django.contrib.auth.models import User

class VehicleType(models.Model):
    name = models.CharField(max_length=50) # e.g., Sedan, SUV, Micro
    seats = models.IntegerField(default=4)
    image = models.ImageField(upload_to='cabs/vehicle_types/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.seats} Seats)"

class CabFeature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=100, help_text="Material symbol or FontAwesome class")

    def __str__(self):
        return self.title

class CabFAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question

class Cab(models.Model):
    FUEL_CHOICES = (
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('EV', 'Electric'),
    )

    title = models.CharField(max_length=100, help_text="e.g., Camry, Accord")
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    is_ac = models.BooleanField(default=True)
    seats = models.IntegerField(default=4)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=4.5)
    
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.IntegerField(default=0)
    
    included_kms = models.IntegerField(default=600)
    price_per_extra_km = models.DecimalField(max_digits=6, decimal_places=2, default=15.00)
    
    max_luggage = models.IntegerField(default=2)
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES, default='Diesel')
    
    cancellation_policy = models.CharField(max_length=200, default="Free Cancellation, till 1 hour of Pick up")
    waiting_policy = models.CharField(max_length=200, default="Free waiting up to 45 minutes")
    
    primary_image = models.ImageField(upload_to='cabs/main/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.vehicle_type.name}"
        
    def discounted_price(self):
        if self.discount_percentage > 0:
            discount_amount = (self.base_price * self.discount_percentage) / 100
            return self.base_price - discount_amount
        return self.base_price

class CabImage(models.Model):
    cab = models.ForeignKey(Cab, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='cabs/gallery/')

    def __str__(self):
        return f"Image for {self.cab.title}"

class CabBooking(models.Model):
    TRIP_CHOICES = (
        ('oneway', 'One Way'),
        ('round', 'Round Trip'),
    )
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    cab = models.ForeignKey(Cab, on_delete=models.SET_NULL, null=True)
    trip_type = models.CharField(max_length=20, choices=TRIP_CHOICES, default='oneway')
    
    pickup_city = models.CharField(max_length=100)
    drop_city = models.CharField(max_length=100)
    pickup_date = models.DateField()
    pickup_time = models.TimeField()
    
    pickup_address = models.CharField(max_length=255, blank=True)
    drop_address = models.CharField(max_length=255, blank=True)
    
    # Traveler Info
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.id} - {self.first_name} {self.last_name}"
