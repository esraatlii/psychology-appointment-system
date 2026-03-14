from django.contrib import admin
from .models import Psychologist, GalleryImage, Education, Workspaces, WorkingHours


@admin.register(WorkingHours)
class WorkingHoursAdmin(admin.ModelAdmin):
    list_display = ("get_day_display", "open_time", "close_time", "is_closed")
    list_editable = ("open_time", "close_time", "is_closed")
    ordering = ("day",)


@admin.register(Psychologist)
class PsychologistAdmin(admin.ModelAdmin):
    list_display = ("full_name", "title", "city", "is_active", "is_online", "is_in_person")
    list_editable = ("is_active",)
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        ("Kimlik Bilgileri", {
            "fields": ("full_name", "title", "profile_image")
        }),
        ("Biyografi & İçerik", {
            "description": "💡 Hero bölümünde 'Kısa Tanıtım', Hakkımda sayfasında 'Ayrıntılı Özgeçmiş' gösterilir.",
            "fields": ("short_bio", "about_preview", "about_full")
        }),
        ("Çalışma Biçimi", {
            "fields": ("is_online", "is_in_person")
        }),
        ("İletişim", {
            "fields": ("email", "phone", "city")
        }),
        ("Yönetim", {
            "fields": ("is_active", "order", "created_at", "updated_at"),
            "classes": ("collapse",)
        }),
    )


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("__str__", "psychologist", "category", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter = ("category",)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("title", "education")


@admin.register(Workspaces)
class WorkspacesAdmin(admin.ModelAdmin):
    list_display = ("title", "definition")