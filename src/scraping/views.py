from django.shortcuts import render
from .models import Vacamcy

def home_view(request):
    gs = Vacamcy.objects.all()
    return render(request, 'home_html', {'object_list': gs})


