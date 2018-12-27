from django.shortcuts import render
from . import froms
# Create your views here.

def index(request):
    return render(request, 'index.html')

def form_name(request):
    ffc = froms.FormName()
    return render(request, 'form_page.html', {'form': ffc})