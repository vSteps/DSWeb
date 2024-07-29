from django.urls import path
from . import views

app_name = 'enquetes'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetalhesView.as_view(), name='detalhes'),
    path('<int:pk>/resultado/', views.ResultadoView.as_view(), name='resultado'),
    path('<int:pergunta_id>/votacao', views.votacao, name='votacao'),


]
    # URL "/enquetes/" --> lista geral das enquetes
    # URL "/enquetes/5/" --> detalhes da enquete com "id" 5
    # URL "/enquetes/5/resultados" --> resultados da enquete com "id" 5
    # URL "/enquetes/5/votacao" --> votacao da enquete com "id" 5