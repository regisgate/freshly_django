from django.contrib import admin
from django.utils.html import format_html
from .models import Categorie, Plat, Temoin

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nom",)}
    search_fields = ("nom",)
    list_display = ("nom", "thumb")
    def thumb(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:40px;border-radius:6px;">', obj.image.url)
        return "—"

@admin.register(Plat)
class PlatAdmin(admin.ModelAdmin):
    list_display = ("nom", "categorie", "prix", "is_disponible", "thumb")
    list_filter = ("categorie", "is_disponible")
    search_fields = ("nom", "description")
    def thumb(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:40px;border-radius:6px;">', obj.image.url)
        return "—"

@admin.register(Temoin)
class TemoinAdmin(admin.ModelAdmin):
    list_display = ("nom", "note", "created_at")
    search_fields = ("nom", "message")
