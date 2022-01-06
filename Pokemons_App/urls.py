from django.urls import path
from . import views

urlpatterns = [
    path('', views.Query_Results, name='Query_Results')

]