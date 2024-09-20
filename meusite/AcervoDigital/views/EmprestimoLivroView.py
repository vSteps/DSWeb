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
