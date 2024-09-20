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
