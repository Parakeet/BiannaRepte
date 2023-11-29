# celra/admin.py
from django.contrib import admin
from django.urls import path
from django.shortcuts import render, get_object_or_404
from .models import Client, Comanda, DetallVenda

admin.site.register(Client)
#admin.site.register(Comanda, ComandaAdmin)
admin.site.register(Comanda)
admin.site.register(DetallVenda)
