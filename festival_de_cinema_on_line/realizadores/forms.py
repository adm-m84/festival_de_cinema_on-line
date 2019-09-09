from django import forms

from .models import *


class RealizadorForm(forms.ModelForm):
    class Meta:
        model = RealizadorModel
        fields = [
            'nome',
            'data_de_nascimento',
            'sexo',
            'email',
            'funcao',
            'foto',
        ]
