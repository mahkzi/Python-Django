from django.contrib import admin
from libros.models import Libro

class LibroAdmin(admin.ModelAdmin):
    list_display = ["titulo", "autor", "precio", "editorial", "fecha_publicacion"]
    search_fields = ["titulo", "autor", "editorial"]

admin.site.register(Libro, LibroAdmin)