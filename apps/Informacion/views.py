from django.shortcuts import render
from .models import Informacion

def index(request):
    context={
        "Informacion": Informacion.objects.first()
    }
    return render(request, 'index.html', context=context)
