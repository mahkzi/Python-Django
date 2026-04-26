from django.shortcuts import render, redirect
from libros.forms import BusquedaLibro, CreacionLibro
from libros.models import Libro

def listado(request):
    formulario_busqueda = BusquedaLibro(request.GET)
    if formulario_busqueda.is_valid():
            libros = Libro.objects.filter(
                titulo__icontains=formulario_busqueda.cleaned_data["titulo"],
                autor__icontains=formulario_busqueda.cleaned_data["autor"],
            )
    else:
        libros = Libro.objects.all()
    return render(request, "libros/listado.html",{"formulario_busqueda": formulario_busqueda, "libros": libros})

def detalle (request, id_libro):
    libro = Libro.objects.get(id=id_libro)
    return render(request, "libros/detalle.html",{"libro":libro})

def crear(request):
    if request.method == "POST":
        formulario_creacion = CreacionLibro(request.POST, request.FILES)
        if formulario_creacion.is_valid():
            formulario_creacion.save()
            return redirect("libros:listado")
    else:
        formulario_creacion = CreacionLibro()
    return render(request, "libros/crear_nuevo.html", {"formulario_creacion": formulario_creacion})