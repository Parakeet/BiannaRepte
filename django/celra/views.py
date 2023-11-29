# celra/views.py
from django.shortcuts import render
from .models import Comanda,Client

def detalls_comanda(request, comanda_id):
    comanda = Comanda.objects.get(pk=comanda_id)
    detalls_comanda = comanda.detallvenda_set.all()

    return render(request, 'celra/detall_comanda.html', {'comanda': comanda, 'detalls_comanda': detalls_comanda})


