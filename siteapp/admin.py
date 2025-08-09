from django.contrib import admin
from .models import Categorie, Plat, Temoin

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nom",)}
    search_fields = ("nom",)

@admin.register(Plat)
class PlatAdmin(admin.ModelAdmin):
    list_display = ("nom", "categorie", "prix", "is_disponible")
    list_filter = ("categorie", "is_disponible")
    search_fields = ("nom", "description")

@admin.register(Temoin)
class TemoinAdmin(admin.ModelAdmin):
    list_display = ("nom", "note", "created_at")
    search_fields = ("nom", "message")
