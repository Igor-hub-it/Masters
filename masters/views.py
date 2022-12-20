from django.shortcuts import render, redirect
from .models import Master
from django.core.paginator import Paginator
from .forms import MasterForm

def home(request):
    masters = Master.objects.all()
    paginator = Paginator(masters, 4)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    data = {
        'masters': masters,
    }
    return render(request, 'masters/home.html', {'page_obj': page_objects})

def add_master(request):
    if request.method == "POST":
        form = MasterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Master.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = MasterForm()
    return render(request, 'masters/add_master.html', {'form': form,})