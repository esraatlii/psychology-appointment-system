from django.contrib import admin
from django.utils.html import format_html
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone", "email", "date", "start_time", "end_time", "status_badge", "created_at")
    list_filter = ("status", "date")
    search_fields = ("full_name", "phone", "email")
    ordering = ("-date", "start_time")
    readonly_fields = ("end_time", "created_at", "status_badge")

    fieldsets = (
        ("Kişisel Bilgiler", {
            "fields": ("full_name", "phone", "email")
        }),
        ("Randevu Zamanı", {
            "fields": ("date", "start_time", "end_time")
        }),
        ("Durum ve Not", {
            "fields": ("status", "note")
        }),
        ("Sistem", {
            "fields": ("created_at",),
            "classes": ("collapse",)
        }),
    )

    # Renkli status badge
    @admin.display(description="Durum", ordering="status")
    def status_badge(self, obj):
        colors = {
            "pending":   ("#fff3cd", "#856404", "⏳ Beklemede"),
            "confirmed": ("#d1fae5", "#065f46", "✅ Onaylandı"),
            "cancelled": ("#fee2e2", "#991b1b", "❌ İptal"),
        }
        bg, color, label = colors.get(obj.status, ("#f3f4f6", "#374151", obj.status))
        return format_html(
            '<span style="background:{};color:{};padding:3px 10px;border-radius:12px;font-size:12px;font-weight:600">{}</span>',
            bg, color, label
        )

    # Listede status'u inline dropdown ile değiştir
    def get_list_editable(self, request):
        return ("status",) if request.user.is_superuser else ()

    # Bekleyen randevu sayacı
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        pending = Appointment.objects.filter(status="pending").count()
        if pending:
            extra_context["subtitle"] = f"⏳ {pending} onay bekleyen randevu var"
        return super().changelist_view(request, extra_context=extra_context)