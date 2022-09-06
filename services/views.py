from django.shortcuts import render
from services.models import service 

# Create your views here.

def Services(request):

    varServices = service.objects.all()
    return render(request, 'Services/services.html', {'varServices': varServices})
