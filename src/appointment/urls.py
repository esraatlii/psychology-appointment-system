from django.urls import path
from . import views

urlpatterns = [
    path('', views.appointment, name='appointment'),
    path('available-slots/', views.get_available_slots, name='available_slots'),
]