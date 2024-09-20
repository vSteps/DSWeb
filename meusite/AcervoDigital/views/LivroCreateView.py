@method_decorator(login_required, name='dispatch')
class LivroCreateView(CreateView):
    model = Livro
    form_class = LivroForm
    template_name = 'cadastrarLivro.html'
    success_url = reverse_lazy('AcervoDigital:index')
