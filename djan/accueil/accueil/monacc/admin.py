from django.contrib import admin
from . models import Produit

class produitadmin(admin.ModelAdmin):
    list_display = ('image', 'nom', 'prix', 'description')

admin.site.register(Produit, produitadmin)


# Register your models here.
