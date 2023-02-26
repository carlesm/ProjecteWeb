from django.shortcuts import render
from django.http import HttpResponse
from web.models import Bar, Tapa
from django.views import generic

# Create your views here.

def home(request):
    bars = Bar.objects.all()[:5]
    dades = {
        'bars': bars,
    }
    resposta = [bar.name for bar in bars]
    return HttpResponse("<br/>".join(resposta))
