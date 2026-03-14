from datetime import datetime, timedelta
from django.db import models


class Appointment(models.Model):
    STATUS = [
        ("pending", "Beklemede"),
        ("confirmed", "Onaylandı"),
        ("cancelled", "İptal"),
    ]

    # Kullanıcı bilgileri
    full_name = models.CharField("Ad-Soyad", max_length=120)
    phone = models.CharField("Telefon Numarası", max_length=20)
    email = models.EmailField("E-posta", blank=True, null=True)

    # Randevu zamanı
    date = models.DateField("Tarih")
    start_time = models.TimeField("Randevu Saati")
    end_time = models.TimeField("Bitiş Saati", editable=False)

    # Durum + opsiyonel not
    status = models.CharField("Durum", max_length=20, choices=STATUS, default="pending")
    note = models.TextField("Not", blank=True, null=True)

    # Sistem alanları
    created_at = models.DateTimeField("Oluşturulma", auto_now_add=True)

    class Meta:
        verbose_name = "Randevu"
        verbose_name_plural = "Randevular"
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["date", "start_time"],
                name="unique_appointment_slot",
                violation_error_message="Bu tarih ve saat için zaten bir randevu bulunmaktadır."
            )
        ]

    def save(self, *args, **kwargs):
        # 1 seans = 60 dakika → end_time otomatik hesaplanır
        start_dt = datetime.combine(self.date, self.start_time)
        end_dt = start_dt + timedelta(hours=1)
        self.end_time = end_dt.time()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} - {self.date} {self.start_time.strftime('%H:%M')}"
