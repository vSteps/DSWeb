from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView
from .forms import EmprestimoLivroForm, RegistroUsuarioForm, ContatoForm
from .forms import LivroForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import Livro, Contato
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.urls import reverse_lazy


# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):
        livros = Livro.objects.all()
        return render(request, "acervo/index.html", {'livros': livros})

class Listarlivros(View):
    def get(self, request, *args, **kwargs):
        livros = Livro.objects.all()
        livros_disp = Livro.objects.filter(disponivel=True)
        livros_indisp = Livro.objects.filter(disponivel=False)

        context = {
            'livros': livros,
            'livros_disp': livros_disp,
            'livros_indisp': livros_indisp,
            }
        return render(request, "acervo/listarLivros.html", context)

@method_decorator(login_required, name='dispatch')
class EmprestimoLivroView(UpdateView):
    model = Livro
    form_class = EmprestimoLivroForm
    template_name = 'emprestarLivro.html'
    success_url = reverse_lazy('AcervoDigital:index')

    def form_valid(self, form):
        livro = form.save(commit=False)
        livro.disponivel = False
        livro.save()
        contato = form.cleaned_data['contato']  # Pega o contato escolhido
        livro.contato = contato  # Associa o contato ao livro
        livro.save()
        messages.success(self.request, f'O livro "{livro.nome}" foi emprestado com sucesso!')
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class DevolverLivroView(View):
    def post(self, request, *args, **kwargs):
        livro_id = kwargs['pk']
        livro = get_object_or_404(Livro, pk = livro_id)
        livro.disponivel = True
        livro.contato_pessoal = None
        livro.save()
        return redirect("AcervoDigital:index")


## FORMS ##


class RegistroUsuarioView(CreateView):
    model = User
    form_class = RegistroUsuarioForm
    template_name = 'registrar.html'
    success_url = reverse_lazy('AcervoDigital:index')

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        if user:
            login(self.request, user)
            messages.success(self.request, 'Cadastro realizado com sucesso!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao cadastrar. Por favor, verifique os dados.')
        return super().form_invalid(form)

@method_decorator(login_required, name='dispatch')
class LivroCreateView(CreateView):
    model = Livro
    form_class = LivroForm
    template_name = 'cadastrarLivro.html'
    success_url = reverse_lazy('AcervoDigital:index')

@method_decorator(login_required, name='dispatch')
class ContatoCreateView(CreateView):
    model = Contato
    form_class = ContatoForm
    template_name = 'cadastrarContato.html'
    success_url = reverse_lazy('AcervoDigital:index')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
