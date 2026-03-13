from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage,name='homepage'),
    path('aboutme/', views.aboutme,name='aboutme'),
    path('gallery/', views.gallery,name='gallery'),
    path('opinion/', views.opinion,name='opinion'),
    path('services/', views.services,name='services'),
    path('workinghours/',views.workinghours,name="workinghours")


]