#from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import PlaceRemember


class HomeView(TemplateView):
    template_name = 'places_app/index.html'


class PlaceCreateView(CreateView):
    model = PlaceRemember
    template_name = 'places_app/add-place.html'
    success_url = reverse_lazy('home')
    fields = ['place_name', 'comment']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
