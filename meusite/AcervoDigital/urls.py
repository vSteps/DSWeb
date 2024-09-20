from . import views
from django.urls import path

app_name = "AcervoDigital"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('item/<int:pk>/', views.ItemView.as_view(), name='item'),
    path('lista', views.Listarlivros.as_view(), name='lista'),
    path('explorar', views.Listarlivros.as_view(), name='explorar'),
    path('cadastrarLivro/', views.LivroCreateView.as_view(), name='cadastrarLivro'),
    path('cadastrarContato/', views.ContatoCreateView.as_view(), name='cadastrarContato'),
    path('livro/<int:pk>/emprestar/', views.EmprestimoLivroView.as_view(), name='emprestarLivro'),
    path('registrar/', views.RegistroUsuarioView.as_view(), name='registrar'),
]