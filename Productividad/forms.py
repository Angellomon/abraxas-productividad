from django import forms
from .models import Tarea

class FormTarea(forms.ModelForm):
    class Meta():
        model = Tarea
        fields = ('nombre', 'descripcion', 'h_inicio', 'm_inicio', 's_inicio')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'input-nombre'}),
            'descripcion': forms.Textarea(attrs={'class': 'input-descripcion'}),
            'h_inicio': forms.NumberInput(attrs={'min': '0', 'max': '1'}),
            'm_inicio': forms.NumberInput(attrs={'min': '0', 'max': '60'}),
            's_inicio': forms.NumberInput(attrs={'min': '0', 'max': '60'}),
        }
        labels = {
            'h_inicio': 'Horas',
            'm_inicio': 'Minutos',
            's_inicio': 'Segudos',
        }
