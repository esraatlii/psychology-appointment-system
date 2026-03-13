from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Formunuz başarıyla gönderilmiştir")
            return redirect("contact")  # aynı sayfaya redirect
        else:
            messages.error(request,"İşleminiz başarısız")
    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form})

