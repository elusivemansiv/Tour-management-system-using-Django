from django.db import models

class FlightOffer(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    discount_percentage = models.IntegerField(default=0)
    image = models.ImageField(upload_to='flights/offers/', blank=True, null=True)
    
    def __str__(self):
        return self.title

class PopularDestination(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to='flights/destinations/')
    flight_count = models.IntegerField(default=1)
    
    def __str__(self):
        return self.city

class Flight(models.Model):
    TRIP_TYPES = (
        ('Oneway', 'Oneway'),
        ('Roundtrip', 'Roundtrip'),
        ('Multi-city', 'Multi-city'),
    )
    
    airline = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='airlines/', blank=True, null=True)
    trip_type = models.CharField(max_length=20, choices=TRIP_TYPES, default='Oneway')
    
    # Origin and Dest here act as main summary (e.g. initial departure to final arrival)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    
    base_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    # Optional return flight fields for simple round trip
    return_departure_time = models.DateTimeField(blank=True, null=True)
    return_arrival_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.airline} - {self.origin} to {self.destination}"
        
    def total_duration(self):
        diff = self.arrival_time - self.departure_time
        hours = diff.seconds // 3600
        minutes = (diff.seconds % 3600) // 60
        return f"{hours}h {minutes}m"

class FlightSegment(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='segments')
    airline = models.CharField(max_length=100)
    flight_number = models.CharField(max_length=20)
    
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    
    layover_duration = models.CharField(max_length=50, blank=True, help_text="e.g. 5h 50m")
    
    def __str__(self):
        return f"{self.flight_number} - {self.origin} to {self.destination}"

    def duration(self):
        diff = self.arrival_time - self.departure_time
        hours = diff.seconds // 3600
        minutes = (diff.seconds % 3600) // 60
        return f"{hours}h {minutes}m"

class FlightFare(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='fares')
    name = models.CharField(max_length=50) # e.g. Basic, Standard, Premium
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cabin_class = models.CharField(max_length=50, choices=[
        ('Economy', 'Economy'),
        ('Business', 'Business'),
        ('First Class', 'First Class')
    ], default='Economy')
    
    is_refundable = models.BooleanField(default=False)
    baggage_info = models.CharField(max_length=100, default='1x 23kg check-in, 1x 7kg cabin')
    features = models.TextField(blank=True, help_text="Comma separated features")
    
    def __str__(self):
        return f"{self.name} fare for {self.flight}"
