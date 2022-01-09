from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Query_Results', views.Query_Results, name='Query_Results'),
    path('add_a_pokemon', views.add_a_pokemon, name='add_a_pokemon')
]