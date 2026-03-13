from django import forms
from .models import Appointment
from pages.models import WorkingHours
from django.utils import timezone
from datetime import datetime,timedelta


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["full_name", "phone", "email", "date", "start_time", "note"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "start_time": forms.TimeInput(attrs={"type": "time"}),
            "note": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Bootstrap class
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

    def clean_date(self):
        selected_date = self.cleaned_data.get("date")
        today = timezone.localdate()
        
        if selected_date and selected_date < today:
            raise forms.ValidationError("Geçmiş bir tarih seçemezsiniz.")
        else:
            return selected_date
    
    def clean(self):
        cleaned_data = super().clean()

        selected_date = cleaned_data.get("date")
        start_time =cleaned_data.get("start_time")
        
        if not selected_date or not start_time:
            return cleaned_data
        
        day_index = selected_date.weekday()

        wh = WorkingHours.objects.filter(day=day_index).first()
        if not wh:
            raise forms.ValidationError("Bu gün için çalışma tanımlı değil")
        if wh.is_closed:
            raise forms.ValidationError("Seçtiğiniz gün kapalı. Lütfen başka bir gün seçiniz.")
        # Sadece saat başı seçilebilsin (09:00, 10:00, ...)
        if start_time.minute != 0 or start_time.second != 0:
            raise forms.ValidationError("Lütfen saat başı seçiniz (09:00, 10:00 gibi).")

        if start_time < wh.open_time:
            raise forms.ValidationError("Seçtiğiniz saat çalışma saatleri dışında.")
        
        #start_time + 1 saat <= close_time
        #(1 seans = 60 dakika)
        start_dt = datetime.combine(selected_date,start_time)
        end_dt = start_dt + timedelta(hours=1)

        if end_dt.time() > wh.close_time:
            raise forms.ValidationError("Seçtiğiniz saat seans süresiyle birlikte çalışma saatlerini aşıyor.")

        exists = Appointment.objects.filter(date=selected_date,start_time=start_time).exclude(status="cancelled").exists() #varsa True, yoksa False
        if exists:
            raise forms.ValidationError("Bu saat dolu. Lütfen başka bir saat seçin.")
        return cleaned_data
        
        


        
