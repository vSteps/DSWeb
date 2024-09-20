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
