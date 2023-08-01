from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.shortcuts import render
from django.urls import reverse_lazy

from .mixins import UserAccessMixin
from .models import PlaceRemember


class HomeView(TemplateView):
    template_name = 'places_app/index.html'


class PlacesListView(LoginRequiredMixin, ListView):
    model = PlaceRemember
    template_name = 'places_app/my-places.html'
    context_object_name = 'places'

    def get_queryset(self):
        return PlaceRemember.objects.filter(author=self.request.user)


class PlaceCreateView(LoginRequiredMixin, CreateView):
    model = PlaceRemember
    template_name = 'places_app/place-form.html'
    success_url = reverse_lazy('my_places')
    fields = ['location', 'place_name', 'comment']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PlaceUpdateView(UserAccessMixin, UpdateView):
    model = PlaceRemember
    template_name = 'places_app/place-update.html'
    success_url = reverse_lazy('my_places')
    fields = ['location', 'place_name', 'comment']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        place = self.get_object()
        if place.author == self.request.user:
            return True
        return False


class PlaceDeleteView(UserAccessMixin, DeleteView):
    model = PlaceRemember
    template_name = 'places_app/place-delete.html'
    success_url = reverse_lazy('my_places')

    def test_func(self):
        place = self.get_object()
        if place.author == self.request.user:
            return True
        return False


def error404(request, exception):
    return render(request, 'places_app/404.html')


def error403(request, exception):
    return render(request, 'places_app/403.html')
