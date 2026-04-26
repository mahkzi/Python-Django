from django.urls import path
from libros.views import listado

app_name = "libros"

urlpatterns = [
    path("", listado, name="listado"),
]
