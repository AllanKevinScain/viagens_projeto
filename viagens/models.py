from django.db import models
from clientes.models import Cliente

class Viagem(models.Model):
    destino = models.CharField(max_length=100)
    data_partida = models.DateField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    clientes = models.ManyToManyField(Cliente)

    def __str__(self):
        return self.destino


