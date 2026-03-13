from django import forms
from .models import ContactMessage
import re

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["full_name", "phone", "email", "subject", "message"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Tüm inputlara Bootstrap class
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})

        # Mesaj textarea'sını güzelleştir
        self.fields["message"].widget.attrs.update({"rows": 4})

    # 1) Telefon için tek alan validasyonu
    def clean_phone(self):
        phone = (self.cleaned_data.get("phone") or "").strip()

        # Telefon boş olursa hata 
        if not phone:
            raise forms.ValidationError("Telefon numarası boş bırakılamaz")


        # Sadece rakam kalsın (boşluk, -, () gibi şeyleri temizle)
        digits = re.sub(r"\D", "", phone)

        # Örnek kural: Türkiye'de 10-11 haneli olsun (0532... gibi)
        if len(digits) < 10 or len(digits) > 11:
            if not (digits.startswith("0") or digits.startswith("9")):
                raise forms.ValidationError("Telefon numarası 0 veya 9 ile başlamalıdır.")
            raise forms.ValidationError("Telefon numarası 10-11 haneli olmalı.")

        return digits  

    # 2) Subject alanı için: min uzunluk + sadece sayı olmasın
    def clean_subject(self):
        subject = (self.cleaned_data.get("subject") or "").strip()

        if not subject:
            raise forms.ValidationError("Konu alanı boş bırakılamaz.")

        if len(subject) < 3:
            raise forms.ValidationError("Konu en az 3 karakter olmalı.")

        if subject.isdigit():
            raise forms.ValidationError("Konu sadece sayı olamaz.")

        return subject

    # 3) Message alanı için: min uzunluk + sadece sayı olmasın
    def clean_message(self):
        msg = (self.cleaned_data.get("message") or "").strip()

        if not msg:
            raise forms.ValidationError("Mesaj boş bırakılamaz.")

        if len(msg) < 10:
            raise forms.ValidationError("Mesaj en az 10 karakter olmalı.")

        if msg.isdigit():
            raise forms.ValidationError("Mesaj sadece sayı olamaz.")

        return msg

