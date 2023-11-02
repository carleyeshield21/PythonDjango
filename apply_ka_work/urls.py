from django.urls import path
from . import views

urlpatterns = [
    path('', views.hindex, name='hindex'),
    path('about/', views.about, name='about')
]