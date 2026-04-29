from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from usuarios.forms import CreacionUsuarioForm
from django.contrib.auth.decorators import login_required


def iniciar_sesion (request):
    if request.method == "POST":
        formulario_iniciar_sesion = AuthenticationForm(request, data=request.POST)
        if formulario_iniciar_sesion.is_valid():
            usuario = formulario_iniciar_sesion.get_user()
            login(request, usuario)
            return redirect("home:home")
    else:
        formulario_iniciar_sesion = AuthenticationForm()
             
    return render(request,"usuarios/iniciar_sesion.html", {"formulario_iniciar_sesion": formulario_iniciar_sesion})


def registro (request):
    if request.method == "POST":
        formulario_registro = CreacionUsuarioForm(request.POST)
        if formulario_registro.is_valid():
            formulario_registro.save()
            return redirect("usuarios:iniciar_sesion")
    else : 
        formulario_registro = CreacionUsuarioForm()
    return render (request, "usuarios/registro.html", {"formulario_registro":formulario_registro})

@login_required
def perfil(request):
    return render (request, "usuarios/perfil.html")