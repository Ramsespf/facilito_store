from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm


def index(request):
    return render(request, 'index.html', {})

def login_views(request):
    #Metodo para authentificar a un user
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request,user)
            messages.success(request, f'Bienvenido {user.username}')
            redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña invalido')
      
        
    return render(request, 'users/login.html', {})

def logout_views(request):
    logout(request)
    messages.success(request, "Sesion cerrada exitosamente")
    return redirect('login')

def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()

    return render(request, 'users/register.html', {'form':form})

