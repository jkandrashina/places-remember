from django.urls import path
from .views import HomeView, PlaceCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add-place/', PlaceCreateView.as_view(), name='add_place')
]
