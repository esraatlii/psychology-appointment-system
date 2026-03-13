from django.db import models

# Create your models here.

class ContactMessage(models.Model):
    # Kullanıcı Bilgileri
    full_name = models.CharField(verbose_name="Ad-Soyad",max_length=120)
    phone = models.CharField(verbose_name="Telefon",max_length=30)
    email = models.EmailField(verbose_name="E-posta")

    #Mesaj içeriği
    subject = models.CharField(verbose_name="Konu")
    message = models.TextField(verbose_name="Kullanıcı Mesajı")

    #Yönetim alanları
    is_read = models.BooleanField("Okundu",default=False)
    created_at = models.DateField("Gönderilme Tarihi", auto_now_add=True)

    class Meta:
        verbose_name = "İletişim Mesajı"
        verbose_name_plural = "İletişim Mesajları"
        ordering = ["-created_at"] # en yeni en üstte
        
    def __str__(self):
        return f"{self.full_name} - {self.created_at:%d.%m.%Y %H:%M}"
