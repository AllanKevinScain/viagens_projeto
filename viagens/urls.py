from django.urls import path
from .views import viagens, cadastrar_viagem

app_name = 'viagens'

urlpatterns = [
    path("", viagens, name="lista"),
    path("registrar-viagem/", cadastrar_viagem, name="cadastrar"),
]
