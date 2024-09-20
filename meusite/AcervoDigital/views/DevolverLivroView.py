@method_decorator(login_required, name='dispatch')
class DevolverLivroView(View):
    def post(self, request, *args, **kwargs):
        livro_id = kwargs['pk']
        livro = get_object_or_404(Livro, pk = livro_id)
        livro.disponivel = True
        livro.contato_pessoal = None
        livro.save()
        return redirect("AcervoDigital:index")
