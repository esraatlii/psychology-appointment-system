from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,'pages/homepage.html')

def about(request):
    return render(request,'pages/about.html')

def contact(request):
    return render(request,'pages/contact.html')

def gallery(request):
    return render(request,'pages/gallery.html')

def opinion(request):
    return render(request,'pages/opinion.html')

def services(request):
    return render(request,'pages/services.html')
