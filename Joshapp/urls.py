from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL
    path('home/', views.index, name='home'),  # Home URL
    path('index/', views.home, name='index'),  # Home URL


]
