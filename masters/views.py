from django.shortcuts import render
from .models import Master

def home(request):
    masters = Master.objects.all()
    data = {
        'maters': masters,
    }
    return render(request, 'masters/home.html', data)