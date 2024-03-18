from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Pergunta
# Create your views here.

def index(request):
    lista_ultima_pergunta = Pergunta.objects.order_by('-data_publicacao') [:5]
    contexto = {
        'lista_ultima_pergunta': lista_ultima_pergunta,
        }

    # Para acessar o banco de dados:
        #saida = ', '.join([q.texto_pergunta for q in lista_ultima_pergunta])

    # Para usar templates:
        #template = loader.get_template('enquetes/index.html') (em cima de contexto)
            #return HttpResponse(template.render(context, request))

    return render(request, 'enquetes/index.html', contexto)

def detalhe(request, pergunta_id):
    resultado = "Você está visualizando a pergunta %s."
    return HttpResponse(resultado % pergunta_id)

def resultados(request, pergunta_id):
    resultado = "Resultados da pergunta %s."
    return HttpResponse(resultado % pergunta_id)

def votacao(request, pergunta_id):
    resultado = "Votação para a pergunta %s."
    return HttpResponse(resultado % pergunta_id)

