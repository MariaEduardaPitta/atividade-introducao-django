
from django.db import models


class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    ano_publicacao = models.IntegerField()

    def __str__(self):
        return self.titulo


class Atividade(models.Model):
    titulo = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    frequencia = models.CharField(max_length=50)
    prioridade = models.IntegerField()

    def __str__(self):
        return self.titulo
