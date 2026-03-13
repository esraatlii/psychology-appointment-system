from django.shortcuts import redirect, render
from .forms import AppointmentForm
from django.contrib import messages

def appointment(request):
    timeslots = ["09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00"]

    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Randevunuz başarıyla alınmıştır")
            return redirect("appointment")
        else:
            messages.error(request,"İşleminiz başarısız")
    else:
        form = AppointmentForm()
        return render(request,"appointment/appointment.html",{"form":form,"timeslots": timeslots})
    return render(request,"appointment/appointment.html",{"form":form,"timeslots": timeslots})
