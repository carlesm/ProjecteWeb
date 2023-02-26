from django.shortcuts import render
from django.http import HttpResponse
from web.models import Bar, Tapa
from django.views import generic

# Create your views here.

# def home(request):
#     bars = Bar.objects.all()[:5]
#     dades = {
#         'bars': bars,
#     }
#     resposta = [bar.name for bar in bars]
#     return HttpResponse("<br/>".join(resposta))

def home(request):
    bars = Bar.objects.all()[:5]
    return render(request, "web/index.html", {"bars": bars})


def bar(request, bar_id):
    try:
        bar = Bar.objects.get(pk=bar_id)
    except Bar.DoesNotExist:
        raise Http404("Aquest Bar no existeix")
    return render(request, 'web/bar.html', {'bar': bar})

class TapaView(generic.DetailView):
    model = Tapa
    template_name = 'web/tapa.html'
