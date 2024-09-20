from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

class Contato(models.Model):
    telefone = models.CharField(max_length=15)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.email

class Livro(models.Model):
    nome = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 50)
    ano = models.DateField("Data de Publicação")
    imagem = models.ImageField(upload_to = 'media/')
    disponivel = models.BooleanField(default=True)
    contato = models.ForeignKey(Contato, null=True, blank=True, on_delete=models.SET_NULL)