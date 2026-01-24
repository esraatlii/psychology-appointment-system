from django.db import models

class Psychologist(models.Model):
    # Temel kimlik
    full_name = models.CharField("Ad Soyad", max_length=100)
    title = models.CharField("Ünvan", max_length=100, blank=True)  # Klinik Psikolog vb.

    # Profil sayfasında görünen içerikler
    short_bio = models.TextField("Kısa Tanıtım (Özet)", blank=True)  # kart üstündeki paragraf
    about_preview = models.TextField("Birkaç Kelime ile (Kısa)", blank=True)  # Hakkımda kutusu (kısa)
    about_full = models.TextField("Ayrıntılı Özgeçmiş (Uzun)", blank=True)  # 'Tümünü Göster' / detay sayfa

    # Medya
    profile_image = models.ImageField(
        "Profil Fotoğrafı",
        upload_to="psychologists/profile/",
        blank=True,
        null=True
    )

    # Çalışma biçimi
    is_online = models.BooleanField("Online Görüşme Var", default=True)
    is_in_person = models.BooleanField("Yüz Yüze Görüşme Var", default=True)

    # İletişim (istersen gösterirsin / gizlersin)
    email = models.EmailField("E-posta", blank=True)
    phone = models.CharField("Telefon", max_length=30, blank=True)
    city = models.CharField("Şehir", max_length=60, blank=True)

    # Yönetim
    is_active = models.BooleanField("Aktif", default=True)
    order = models.PositiveIntegerField("Sıralama", default=1)
    created_at = models.DateTimeField("Oluşturulma", auto_now_add=True)
    updated_at = models.DateTimeField("Güncellenme", auto_now=True)

    class Meta:
        verbose_name = "Psikolog"
        verbose_name_plural = "Psikologlar"
        ordering = ["order", "full_name"]

    def __str__(self):
        return self.full_name

from django.db import models

class GalleryImage(models.Model):
    CATEGORY_CHOICES = (
        ("certificate", "Sertifika"),
        ("office", "Ofis"),
        ("event", "Etkinlik"),
        ("other", "Diğer"),
    )

    psychologist = models.ForeignKey(
        "Psychologist",
        on_delete=models.CASCADE,
        related_name="gallery_images",
        verbose_name="Psikolog",
    )

    image = models.ImageField(
        "Görsel",
        upload_to="gallery/",
    )

    category = models.CharField(
        "Kategori",
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="other",
    )

    title = models.CharField(
        "Başlık",
        max_length=120,
        blank=True,
    )

    description = models.TextField(
        "Açıklama",
        blank=True,
    )

    order = models.PositiveIntegerField(
        "Sıralama",
        default=1,
    )

    is_active = models.BooleanField(
        "Aktif",
        default=True,
    )

    created_at = models.DateTimeField("Oluşturulma", auto_now_add=True)

    class Meta:
        verbose_name = "Galeri Görseli"
        verbose_name_plural = "Galeri Görselleri"
        ordering = ["order", "-created_at"]

    def __str__(self):
        if self.title:
            return self.title
        return f"Galeri Görseli #{self.id}"

class Education(models.Model):
    university_name = models.CharField(max_length=50,verbose_name="Üniversite Adı")