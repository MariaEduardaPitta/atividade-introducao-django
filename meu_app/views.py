
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Livro, Atividade
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    livros = Livro.objects.all()
    atividades = Atividade.objects.all()

    context = {
        'livros': livros,
        'atividades': atividades
    }

    return render(request, 'index.html', context)


def registrar_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'registro.html', {
                'erro': 'Nome de usuário já existe.'
            })

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return redirect('login')

    return render(request, 'registro.html')


def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        usuario = authenticate(
            request,
            username=username,
            password=password
        )

        if usuario is not None:
            login(request, usuario)
            return redirect('home')

        return render(request, 'login.html', {
            'erro': 'Usuário ou senha incorretos.'
        })

    return render(request, 'login.html')


def logout_usuario(request):
    logout(request)
    return redirect('login')
