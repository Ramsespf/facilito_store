from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html', {
        'message' : 'Listado de Producto',
        'tittle' : 'Productos',
        'products' : [
            {'title':'Playera', 'price': 5, 'stock': True},
            {'title':'Camisa', 'price': 7, 'stock': True},
            {'title':'Mochila', 'price': 25, 'stock': False},
        ]
    })

def login_views(request):
    if request.user.is_authenticated:
        return redirect('index')

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
    if request.user.is_authenticated:
        return redirect('index')

    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado satisfactoriamente')
            return redirect('index')

    return render(request, 'users/register.html', {'form':form})

