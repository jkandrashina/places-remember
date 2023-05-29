from django.urls import path
from .views import HomeView, PlaceCreateView, PlacesListView, PlaceUpdateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('my-places/', PlacesListView.as_view(), name='my_places'),
    path('add-place/', PlaceCreateView.as_view(), name='add_place'),
    path('place/<int:pk>/update', PlaceUpdateView.as_view(), name='update_place'),
]
