from django import forms
from about.models import About

class BaseAboutForm(forms.ModelForm):
    
     class Meta:
        model = About
        fields = "__all__"

class AboutForm(BaseAboutForm):
   ...

class EliminarEnvio(BaseAboutForm):
    ...