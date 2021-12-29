from django.urls import path
from . import views

urlpatterns = [
    path('place-form/', views.place_form, name='place_form'),
    path('', views.places_list, name='home'),
]