from django.shortcuts import render
from . models import Produit

from django.http import HttpResponse

def index(request, *args, **kwargs):


    nbre1 = 55
    nbre2 = 9

    resu = nbre1 + nbre2
    thierry = ['lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche'],

    context = {


        'nbre1':nbre1,
        'nbre2':nbre2,
        'resu': resu,
        'malist':thierry
    }
    return render(request, 'monacc/index.html', context)

def index1(request):
    return render(request, 'monacc/index1.html')
def base(request):
    return render(request, 'monacc/base.html')

def nav(request):
    return render(request, 'monacc/nav.html')

def aff(request):
    produit = Produit.objects.get(id=1)
    context ={
       'produit' :produit
    }
    return render(request, 'monacc/aff.html', context)