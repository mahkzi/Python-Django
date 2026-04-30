from django.urls import path, reverse_lazy
from usuarios.views import registro, iniciar_sesion, perfil, editar_perfil
from django.contrib.auth.views import LogoutView, PasswordChangeView
from usuarios.forms import MiCambioPasswordForm


app_name = "usuarios"

urlpatterns = [
    path("iniciar_sesion/", iniciar_sesion, name="iniciar_sesion"),
    path("registro/", registro, name="registro"),
    path("cerrar_sesion/", LogoutView.as_view(template_name="usuarios/cerrar_sesion.html"), name ="cerrar_sesion"),
    path("perfil/", perfil, name="perfil"),
    path("editar_perfil/", editar_perfil, name="editar_perfil"),
    path("cambiar_password/", PasswordChangeView.as_view(
        template_name="usuarios/cambiar_password.html",
        success_url=reverse_lazy('usuarios:perfil'),
        form_class=MiCambioPasswordForm,
    ), name="cambiar_password"),
]
