from django.shortcuts import render, HttpResponse
from .models import Evento
from core.models import Evento
# Create your views here.
def index(request):
    return render(request, 'index.html')

def evento(request, titulo):
    evento = Evento.objects.get(titulo=titulo)
    return HttpResponse('Evento: {} na data {}'.format(evento.titulo, evento.data_evento))


def lista_eventos(request):

    context = {
        'eventos': Evento.objects.all()
    }
    return render(request, 'agenda.html', context)