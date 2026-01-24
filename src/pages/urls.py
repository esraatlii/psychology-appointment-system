from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage,name='homepage'),
    path('about/', views.aboutme,name='aboutme'),
    path('contact/', views.contact,name='contact'),
    path('gallery/', views.gallery,name='gallery'),
    path('opinion/', views.opinion,name='opinion'),
    path('services/', views.services,name='services'),


]