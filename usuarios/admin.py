from django.contrib import admin
from usuarios.models import Perfil

from django.contrib import admin
from .models import Perfil

@admin.register(Perfil)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["get_username", "get_first_name", "get_last_name", "get_email", "avatar"]
    
    search_fields = ["user__username", "user__email"]
    
    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = "Nombre de Usuario"

    def get_first_name(self, obj):
        return obj.user.first_name  
    get_first_name.short_description = "Nombre"

    def get_last_name(self, obj):
        return obj.user.last_name  
    get_last_name.short_description = "Apellido"

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = "Email"
