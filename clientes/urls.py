from django.urls import path
from .views import clientes, cadastrar_cliente, cliente_viagens

app_name = 'clientes'

urlpatterns = [
    path("", clientes, name="lista"),
    path("registrar-cliente/", cadastrar_cliente, name="cadastrar"),
    path("viagens-por-cliente/<int:cliente_id>", cliente_viagens, name="cliente_viagens"),
]
