from django.urls import path
from .views import HomeView, PlaceCreateView, PlacesListView, PlaceUpdateView, PlaceDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('my-places/', PlacesListView.as_view(), name='my_places'),
    path('add-place/', PlaceCreateView.as_view(), name='add_place'),
    path('place/<int:pk>/update', PlaceUpdateView.as_view(), name='update_place'),
    path('place/<int:pk>/delete', PlaceDeleteView.as_view(), name='delete_place'),
]
