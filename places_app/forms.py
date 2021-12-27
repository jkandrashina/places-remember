from django import forms
from .models import PlaceToRemember

class PlaceForm(forms.ModelForm):
    class Meta:
        model = PlaceToRemember
        fields = ('place_name', 'text', 'address',)