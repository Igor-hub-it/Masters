from .models import Master
from django.forms import ModelForm

class MasterForm(ModelForm):
    class Meta:
        model = Master
        fields = ['name', 'description', 'price', 'experience', 'phone', 'vk']