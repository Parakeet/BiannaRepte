# celra/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<int:comanda_id>/', views.detalls_comanda, name='detall_comanda'),
    # Altres URLs si és necessari
]
