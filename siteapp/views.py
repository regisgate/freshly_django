from django.shortcuts import render
from .models import Plat, Temoin, Categorie

def home(request):
    plats = Plat.objects.filter(is_disponible=True)[:6]
    temoins = Temoin.objects.order_by('-created_at')[:5]
    return render(request, 'home.html', {'plats': plats, 'temoins': temoins})

def menu(request):
    categories = Categorie.objects.all()
    plats = Plat.objects.filter(is_disponible=True)
    return render(request, 'menu.html', {'categories': categories, 'plats': plats})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

