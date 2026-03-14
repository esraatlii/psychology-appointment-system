from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone", "email", "subject", "is_read", "created_at")
    list_filter = ("is_read", "created_at")
    search_fields = ("full_name", "phone", "email", "subject")
    ordering = ("-created_at",)
    list_editable = ("is_read",)
    readonly_fields = ("created_at",)

    fieldsets = (
        ("Gönderen Bilgileri", {
            "fields": ("full_name", "phone", "email")
        }),
        ("Mesaj", {
            "fields": ("subject", "message")
        }),
        ("Durum", {
            "fields": ("is_read", "created_at"),
        }),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs

    # Okunmamış mesaj sayısını liste başlığında göster
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        unread = ContactMessage.objects.filter(is_read=False).count()
        if unread:
            extra_context["subtitle"] = f"📬 {unread} okunmamış mesaj var"
        return super().changelist_view(request, extra_context=extra_context)