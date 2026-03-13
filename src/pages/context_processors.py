from .models import WorkingHours,Psychologist

def footer_context(request):
    return {
        "working_hours": WorkingHours.objects.all(),
        "psychologists" : Psychologist.objects.all()
    }
