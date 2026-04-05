from django.db import models

class Flight(models.Model):
    airline = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cabin_class = models.CharField(max_length=50, choices=[
        ('Economy', 'Economy'),
        ('Business', 'Business'),
        ('First Class', 'First Class')
    ], default='Economy')
    logo = models.ImageField(upload_to='airlines/', blank=True, null=True)

    def __str__(self):
        return f"{self.airline} - {self.origin} to {self.destination}"
