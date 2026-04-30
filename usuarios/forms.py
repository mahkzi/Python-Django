from django import forms
from django.contrib.auth.models import User
from .models import Perfil
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm


class CreacionUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email",]
        help_texts = {
            "username":"Ingrese su nombre de usuario",
            "password1":"Ingrese su contraseña",
            "password2":"Repita su contraseña",
            "email": "Ingrese su correo electrónico"   
        }
        labels ={
            "username":"Nombre de Usuario",
            "password1":"Contraseña",
            "password2": "Repetir Contraseña",
            "email": "Correo Electrónico"
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['password1'].help_text = "La contraseña debe contener al menos 8 caracteres."
        self.fields['password2'].help_text = "Repita la contraseña."
        
class EditarUsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email",]
        labels = {
            "username": "Nombre de Usuario",
            "first_name": "Nombre",
            "last_name": "Apellido",
            "email": "Correo Electrónico"
        }
        help_texts ={
            "username": "Ingrese su nombre de usuario",
            "first_name": "Ingrese su nombre",
            "last_name": "Ingrese su apellido",
            "email": "Ingrese su correo electrónico"
        }

class EditarAvatarForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ["avatar", "hobbies"]
        labels = {
            "avatar": "Imagen de Perfil",
            "hobbies": "Mis Hobbies"
            }
        
class MiCambioPasswordForm(PasswordChangeForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"].label = "Tu contraseña actual"
        self.fields["new_password1"].label = "Nueva contraseña"
        self.fields["new_password2"].label = "Confirma la nueva contraseña"
        
        self.fields["old_password"].help_text ="Ingrese su contraseña actual"
        self.fields["new_password1"].help_text ="Ingrese su nueva contraseña"
        self.fields["new_password2"].help_text ="Confirme su nueva contraseña"