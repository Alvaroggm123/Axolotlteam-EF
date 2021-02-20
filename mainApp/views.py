from django.shortcuts import render
from .models import Ubications
# Create your views here.
def homePage(request):
    return render(request, "home.html")

def mapsPage(request):
    points = Ubications.objects.all()
    context = {'ubications': points}
    return render(request, "maps2.html", context)