from django.urls import path
from libros.views import listado, detalle, crear

app_name = "libros"

urlpatterns = [
    path("", listado, name="listado"),
    path("<int:id_libro>/", detalle, name="detalle"),
    path("crear/", crear, name="crear")
]
