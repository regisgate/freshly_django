from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nom

class Plat(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    prix = models.DecimalField(max_digits=6, decimal_places=2)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True)
    is_disponible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

class Temoin(models.Model):
    nom = models.CharField(max_length=120)
    message = models.TextField()
    note = models.PositiveSmallIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} ({self.note}/5)"
