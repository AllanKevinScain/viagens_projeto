from django import forms
from .models import Viagem, Cliente

class ViagemForm(forms.ModelForm):
    clientes = forms.ModelMultipleChoiceField(
        queryset=Cliente.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Selecione os Clientes"
    )

    data_partida = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d'],
        label="Data da Partida"
    )

    class Meta:
        model = Viagem
        fields = ['destino', 'data_partida', 'preco', 'clientes']