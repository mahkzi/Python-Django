from django.shortcuts import render, redirect
from about.models import About
from about.forms import AboutForm
from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy

class CrearAbout(CreateView):
    model = About
    form_class = AboutForm
    template_name = "about/about.html"
    success_url = reverse_lazy("about:about")
    
def contacto(request):
    if request.method == "POST":
        formulario_creacion = AboutForm(request.POST,)
        if formulario_creacion.is_valid():
            formulario_creacion.save()
            return redirect("about:envio")
    else:
        formulario_creacion = AboutForm()
    return render(request, "about/contacto.html", {"formulario_creacion": formulario_creacion})

def envio(request):
    return render (request, "about/envio.html")
def mostrar_envio(request):
    info_envio = About.objects.all()
    return render(request, "about/mostrar_envio.html", {"info_envio": info_envio})

class EliminarEnvio(DeleteView):
    model = About
    template_name = "about/eliminar_envio.html"
    success_url = reverse_lazy("about:about")