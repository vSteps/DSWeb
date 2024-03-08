from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>Aplicação de <u>Enquetes</u></h1>\n <h2>Matéria: <u>DSWeb</u></h2>\n <h2>Semestre: <u>2024.1</u></h2>\n <h2>Nome do aluno: <u>Victor Paiva Passos</u></h2>\n <h2>Matrícula: <u>20231014040042</u></h2>')