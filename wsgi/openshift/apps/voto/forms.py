from django import forms
from .models import Participante


class FormParticipante(forms.ModelForm):
    class Meta():
        model = Participante
