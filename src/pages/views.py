from django.http import HttpResponse
from django.shortcuts import render
from .models import Psychologist,GalleryImage,Education,Workspaces,WorkingHours

# Create your views here.

def homepage(request):
    psychologist = Psychologist.objects.first()
    images = GalleryImage.objects.all()
    workspaces = Workspaces.objects.all()

    return render(request,'pages/homepage.html',
                  {'psychologist': psychologist,
                   'images':images,
                   'workspaces':workspaces}
                  )

def aboutme(request):
    psychologist = Psychologist.objects.first()
    educations = Education.objects.all()
    workspaces = Workspaces.objects.all()
    return render(request,'pages/aboutme.html',
                  {'psychologist': psychologist,
                   'educations':educations,
                   'workspaces':workspaces})

def contact(request):
    return render(request,'pages/contact.html')

def gallery(request):
    return render(request,'pages/gallery.html')

def opinion(request):
    return render(request,'pages/opinion.html')

def services(request):
    workspaces = Workspaces.objects.all()

    return render(request,'pages/services.html',{'workspaces':workspaces})

def workinghours(request):
    workinghours = WorkingHours.objects.all()

    return render(request,'pages/_footer.html',{'workinghours':workinghours})
