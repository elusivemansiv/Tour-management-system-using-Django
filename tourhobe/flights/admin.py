from django.contrib import admin
from .models import Flight

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('airline', 'origin', 'destination', 'departure_time', 'price', 'cabin_class')
    search_fields = ('airline', 'origin', 'destination')
    list_filter = ('cabin_class', 'airline')
