from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='locations/', blank=True, null=True)

    def __str__(self):
        return self.name


class Package(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='packages')
    title = models.CharField(max_length=150)
    duration = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='packages/', blank=True, null=True)

    def __str__(self):
        return self.title

class CarouselSlide(models.Model):
    title = models.CharField(max_length=100, blank=True)
    subtitle = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='carousel/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else "Carousel Slide"
