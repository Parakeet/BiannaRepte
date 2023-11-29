# celra/models.py
from django.db import models

class Client(models.Model):
    codi = models.CharField(max_length=10)
    nom = models.CharField(max_length=100)
    nif = models.CharField(max_length=20)
    adreca_fiscal = models.TextField()

class Comanda(models.Model):
    numero_comanda = models.IntegerField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    data_creacio = models.DateField()
    data_necessitat = models.DateField()
    import_comanda = models.DecimalField(max_digits=10, decimal_places=2)
    usuari = models.CharField(max_length=50)

class DetallVenda(models.Model):
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE)
    article = models.TextField()
    descripcio = models.TextField()
    quantitat = models.IntegerField()
    preu_venda = models.DecimalField(max_digits=10, decimal_places=2)
    import_total_linia = models.DecimalField(max_digits=10, decimal_places=2)
