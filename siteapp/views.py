from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .models import Plat, Temoin, Categorie
from .forms import ContactForm


def home(request):
    plats = Plat.objects.filter(is_disponible=True)[:6]
    temoins = Temoin.objects.order_by("-created_at")[:6]
    categories = Categorie.objects.all()
    return render(request, "home.html", {
        "plats": plats,
        "temoins": temoins,
        "categories": categories,
    })


def menu(request):
    categories = Categorie.objects.all()
    plats = Plat.objects.filter(is_disponible=True)
    return render(request, "menu.html", {
        "categories": categories,
        "plats": plats,
    })


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        # Envoi d’email (config SMTP réelle à ajouter plus tard dans settings.py)
        try:
            send_mail(
                subject=f"[Freshly] Message de {data['nom']}",
                message=f"Email: {data['email']}\n\n{data['message']}",
                from_email=getattr(settings, "DEFAULT_FROM_EMAIL", "webmaster@localhost"),
                recipient_list=[getattr(settings, "DEFAULT_TO_EMAIL", "webmaster@localhost")],
                fail_silently=True,
            )
        except Exception:
            pass
        messages.success(request, "Merci ! Votre message a bien été envoyé.")
        return redirect("contact")
    return render(request, "contact.html", {"form": form})


def about(request):
    return render(request, "about.html", {"categories": Categorie.objects.all()})
