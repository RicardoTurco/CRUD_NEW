from django.forms import ModelForm
from .models import Categoria, Transacao

class Categoriaform(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']

class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['data','descricao','valor','categoria','observacoes']
