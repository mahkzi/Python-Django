from django.urls import path
from libros.views import listado, detalle, crear, EditarLibro, EliminarLibro

app_name = "libros"

urlpatterns = [
    path("", listado, name="listado"),
    path("crear/", crear, name="crear"),
    path("<int:id_libro>/", detalle, name="detalle"),
    path("<int:pk>/editar/", EditarLibro.as_view(), name="editar"),
    path("<int:pk>/eliminar/", EliminarLibro.as_view(), name="eliminar"),
]
