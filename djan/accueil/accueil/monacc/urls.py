from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index1', views.index1, name='index1'),
    path('base', views.base, name='base'),
    path('nav', views.nav, name='nav'),
    path('aff', views.aff, name='aff')
]