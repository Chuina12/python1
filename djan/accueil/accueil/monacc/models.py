from django.db import models
from django.contrib import admin



class Produit(models.Model):
    nom = models.CharField(max_length=222)
    prix = models.IntegerField()
    description = models.TextField()

    class Meta:
        verbose_name = ('Produit')

    def __str__(self):
        return self.nom




# Create your models here.

