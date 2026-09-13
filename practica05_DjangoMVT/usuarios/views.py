from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import PerfilUsuario

def login_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('username')
        pass_input = request.POST.get('password')
        
        user = authenticate(request, username=user_input, password=pass_input)
        if user is not None:
            login(request, user)
            try:
                perfil = PerfilUsuario.objects.get(usuario=user)
                rol_nombre = perfil.rol.nombre
            except PerfilUsuario.DoesNotExist:
                rol_nombre = "Sin rol asignado"
                
            messages.success(request, f"¡Bienvenido(a) {user.username}! Tu rol es: {rol_nombre}")
            return redirect('inicio')  # <-- Cambio aquí
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
            
    return render(request, 'usuarios/login.html')

@login_required
def inicio_view(request):
    try:
        perfil = PerfilUsuario.objects.get(usuario=request.user)
        rol_nombre = perfil.rol.nombre
    except PerfilUsuario.DoesNotExist:
        rol_nombre = "Sin rol asignado"

    return render(request, 'usuarios/inicio.html', {
        'rol': rol_nombre
    })