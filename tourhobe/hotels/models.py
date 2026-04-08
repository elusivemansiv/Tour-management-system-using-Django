from django.db import models

class Hotel(models.Model):
    TIER_CHOICES = (
        ('premium', 'Premium'),
        ('budget', 'Budget Friendly'),
        ('standard', 'Standard'),
    )

    name = models.CharField(max_length=150)
    tier = models.CharField(max_length=20, choices=TIER_CHOICES, default='standard')
    location = models.CharField(max_length=150)
    star_rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=3)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    amenities = models.TextField(help_text="Comma separated list of amenities")
    image = models.ImageField(upload_to='hotels/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.get_tier_display()}) - {self.location}"

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    room_type = models.CharField(max_length=100)
    capacity_adults = models.IntegerField(default=2)
    capacity_children = models.IntegerField(default=0)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    total_rooms = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.room_type} - {self.hotel.name}"
