from datetime import datetime, timedelta
from django.shortcuts import redirect, render
from django.http import JsonResponse
from .forms import AppointmentForm
from .models import Appointment
from pages.models import WorkingHours
from django.contrib import messages


def appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Randevunuz başarıyla alınmıştır.")
            return redirect("appointment")
        else:
            messages.error(request, "Lütfen formu eksiksiz ve doğru doldurunuz.")
    else:
        form = AppointmentForm()

    return render(request, "appointment/appointment.html", {"form": form})


def get_available_slots(request):
    """
    AJAX endpoint: ?date=YYYY-MM-DD
    Seçilen güne ait çalışma saatlerini ve dolu slotları döndürür.
    """
    date_str = request.GET.get("date")
    if not date_str:
        return JsonResponse({"error": "Tarih belirtilmedi."}, status=400)

    try:
        selected_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return JsonResponse({"error": "Geçersiz tarih formatı."}, status=400)

    day_index = selected_date.weekday()
    wh = WorkingHours.objects.filter(day=day_index).first()

    if not wh or wh.is_closed or not wh.open_time or not wh.close_time:
        return JsonResponse({"closed": True, "slots": []})

    # Tüm slotları üret (saatlik)
    all_slots = []
    current = datetime.combine(selected_date, wh.open_time)
    end = datetime.combine(selected_date, wh.close_time)

    while current + timedelta(hours=1) <= end:
        all_slots.append(current.strftime("%H:%M"))
        current += timedelta(hours=1)

    # Dolu slotları bul
    booked = set(
        Appointment.objects.filter(
            date=selected_date
        ).exclude(
            status="cancelled"
        ).values_list("start_time", flat=True)
    )
    booked_strs = {t.strftime("%H:%M") for t in booked}

    slots = [
        {"time": t, "available": t not in booked_strs}
        for t in all_slots
    ]

    return JsonResponse({"closed": False, "slots": slots})