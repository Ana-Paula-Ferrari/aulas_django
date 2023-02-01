from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #name usado para criar urls dinamica/ ex.no base.html
    path('sobre/', views.sobre, name='sobre'),
]