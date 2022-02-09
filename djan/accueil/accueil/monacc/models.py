from django.db import models
from django.contrib import admin



class Produit(models.Model):
    image = models.ImageField(upload_to='image', blank=True )
    nom = models.CharField(max_length=222)
    prix = models.IntegerField()
    description = models.TextField()

    class Meta:
        verbose_name = ('Produit')


    def __str__(self):
        return self.nom




# Create your models here.

