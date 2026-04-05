from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    star_rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=3)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    amenities = models.TextField(help_text="Comma separated list of amenities")
    image = models.ImageField(upload_to='hotels/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.location}"
