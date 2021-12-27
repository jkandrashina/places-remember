from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='places_app/home.html'), name='home'),
    path('place-form/', views.place_form, name='place_form'),
    path('my-places/', views.places_list, name='my_places'),
]