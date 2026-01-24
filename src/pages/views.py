from django.http import HttpResponse
from django.shortcuts import render
from .models import Psychologist,GalleryImage

# Create your views here.

def homepage(request):
    psychologist = Psychologist.objects.first()
    images = GalleryImage.objects.all()
    return render(request,'pages/homepage.html',
                  {'psychologist': psychologist,'images':images}
                  )

def aboutme(request):
    return render(request,'pages/aboutme.html')

def contact(request):
    return render(request,'pages/contact.html')

def gallery(request):
    return render(request,'pages/gallery.html')

def opinion(request):
    return render(request,'pages/opinion.html')

def services(request):
    return render(request,'pages/services.html')
