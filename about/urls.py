from django.urls import path
from about.views import CrearAbout, contacto, envio, mostrar_envio, EliminarEnvio

app_name= "about"

urlpatterns = [
    path("", CrearAbout.as_view(), name="about"),
    path("contacto/", contacto, name="contacto"),
    path("contacto/envio/", envio, name="envio"),
    path("mostrar_envio", mostrar_envio, name = "mostrar_envio"),
    path("eliminar_envio/<int:pk>/", EliminarEnvio.as_view(), name="eliminar_envio"),
]
