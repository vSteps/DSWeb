class Livro(models.Model):
    nome = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 50)
    ano = models.DateField("Data de Publicação")
    imagem = models.ImageField(upload_to = 'media/')
    disponivel = models.BooleanField(default=True)
    contato = models.ForeignKey(Contato, null=True, blank=True, on_delete=models.SET_NULL)
