from django.contrib import admin
from .models import PlaceRemember

@admin.register(PlaceRemember)
class PlaceAdmin(admin.ModelAdmin):
    pass