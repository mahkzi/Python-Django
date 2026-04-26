from django import forms
from libros.models import Libro

class BusquedaLibro(forms.Form):
    titulo = forms.CharField(max_length=50, required=False, label="Título")
    autor = forms.CharField(max_length=30, required=False, label="Autor")

class CreacionLibro(forms.ModelForm):
    class Meta:
        model = Libro
        fields = "__all__"
        widgets ={
            "fecha_publicacion": forms.DateInput(attrs={"type": "date"}),
        }