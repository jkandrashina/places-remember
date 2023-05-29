from django.contrib import admin
from .models import PlaceRemember

@admin.register(PlaceRemember)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('place_name', 'author', 'pub_date')
