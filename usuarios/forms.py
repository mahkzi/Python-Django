from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreacionUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]
        help_texts = {
            "username":"Ingrese su nombre de usuario",
            "password1":"Ingrese su contraseña",
            "password2":"Repita su contraseña",
            "email": "Ingrese su correo electrónico"   
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['password1'].help_text = "La contraseña debe contener al menos 8 caracteres."
        self.fields['password2'].help_text = "Repita la contraseña."