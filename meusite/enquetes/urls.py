from django.urls import path
from . import views

app_name = 'enquetes'
urlpatterns = [
    # URL "/enquetes/" --> lista geral das enquetes
    path('', views.index, name='index'),
    # URL "/enquetes/5/" --> detalhes da enquete com "id" 5
    path('<int:pergunta_id>/', views.detalhe, name='detalhe'),
    # URL "/enquetes/5/resultados" --> resultados da enquete com "id" 5
    path('<int:pergunta_id>/resultados/', views.resultados, name='resultado'),
    # URL "/enquetes/5/votacao" --> votacao da enquete com "id" 5
    path('<int:pergunta_id>/votacao', views.votacao, name='votacao'),


]