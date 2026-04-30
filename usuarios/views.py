from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from usuarios.forms import CreacionUsuarioForm, EditarAvatarForm, EditarUsuarioForm
from usuarios.models import Perfil
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

def perfil (request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    return render(request, "usuarios/perfil.html",)

@login_required
def editar_perfil(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form_usuario = EditarUsuarioForm(request.POST, instance=request.user)
        form_avatar = EditarAvatarForm(request.POST, request.FILES, instance=perfil)

        if form_usuario.is_valid() and form_avatar.is_valid():
            form_usuario.save()
            form_avatar.save()
            return redirect("usuarios:perfil")
    else:
        form_usuario = EditarUsuarioForm(instance=request.user)
        form_avatar = EditarAvatarForm(instance=perfil)

    return render(request, "usuarios/editar_perfil.html", {
        "form_usuario": form_usuario,
        "form_avatar": form_avatar
    })