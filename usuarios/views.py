from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm
from .forms import ProfileForm
from .forms import AvatarForm

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('perfil')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def login_usuario(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('perfil')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

def logout_usuario(request):
    logout(request)
    return redirect('login')

@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html')

def editar_perfil(request):
    profile = request.user.profile
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'usuarios/editar_perfil.html', {'form': form})

@login_required
def editar_avatar(request):
    perfil = request.user.profile
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect("perfil")  # redirigir a la vista del perfil
    else:
        form = AvatarForm(instance=perfil)
    return render(request, "usuarios/editar_avatar.html", {"form": form})

@login_required
def editar_avatar(request):
    perfil = request.user.profile  # ✅ instancia del modelo Profile

    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = AvatarForm(instance=perfil)

    return render(request, 'usuarios/editar_avatar.html', {'form': form})
