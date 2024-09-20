@method_decorator(login_required, name='dispatch')
class ContatoCreateView(CreateView):
    model = Contato
    form_class = ContatoForm
    template_name = 'cadastrarContato.html'
    success_url = reverse_lazy('AcervoDigital:index')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)