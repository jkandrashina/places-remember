from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from .models import PlaceRemember


class HomeView(TemplateView):
    template_name = 'places_app/index.html'


class PlacesListView(ListView):
    model = PlaceRemember
    template_name = 'places_app/my-places.html'
    context_object_name = 'places'

    def get_queryset(self):
        return PlaceRemember.objects.filter(author=self.request.user)


class PlaceCreateView(CreateView):
    model = PlaceRemember
    template_name = 'places_app/place-form.html'
    success_url = reverse_lazy('my_places')
    fields = ['place_name', 'comment']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PlaceUpdateView(UpdateView):
    model = PlaceRemember
    template_name = 'places_app/place-update.html'
    success_url = reverse_lazy('my_places')
    fields = ['place_name', 'comment']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
