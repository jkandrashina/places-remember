from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PlaceForm
from .models import PlaceToRemember

@login_required
def place_form(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)
            place.author = request.user
            place.save()
            return redirect('my_places')
    else:
        form = PlaceForm()
    return render(request, 'places_app/place_form.html', {'form': form})

@login_required
def places_list(request):
    places = PlaceToRemember.objects.filter(author=request.user).order_by('pub_date')
    return render(request, 'places_app/my-places.html', {'places': places})
