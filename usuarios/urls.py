from django.urls import path
from usuarios.views import registro, iniciar_sesion, perfil
from django.contrib.auth.views import LogoutView


app_name = "usuarios"

urlpatterns = [
    path("iniciar_sesion/", iniciar_sesion, name="iniciar_sesion"),
    path("registro/", registro, name="registro"),
    path("cerrar_sesion/", LogoutView.as_view(template_name="usuarios/cerrar_sesion.html"), name ="cerrar_sesion"),
    path("perfil/", perfil, name= "perfil")
]
