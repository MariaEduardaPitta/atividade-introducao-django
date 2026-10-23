
from django.shortcuts import render
from .models import Livro, Atividade


def home(request):
    livros = Livro.objects.all()
    atividades = Atividade.objects.all()

    context = {
        'livros': livros,
        'atividades': atividades
    }

    return render(request, 'index.html', context)
