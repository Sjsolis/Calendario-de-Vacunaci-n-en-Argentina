from django import forms
from .models import Enfermedad, GrupoEtario, Vacuna

class EnfermedadForm(forms.ModelForm):
    class Meta:
        model = Enfermedad
        fields = ['nombre', 'descripcion']

class GrupoEtarioForm(forms.ModelForm):
    class Meta:
        model = GrupoEtario
        fields = ['nombre', 'edad_min', 'edad_max']
        labels = {
            'edad_min': 'Edad mínima (meses)',
            'edad_max': 'Edad máxima (meses)',
        }

class VacunaForm(forms.ModelForm):
    class Meta:
        model = Vacuna
        fields = ['nombre', 'enfermedades_previene', 'grupo_etario', 'dosis']

class BusquedaVacunaForm(forms.Form):
    nombre = forms.CharField(required=False, label='Nombre de Vacuna')
    

