class Contato(models.Model):
    telefone = models.CharField(max_length=15)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.email
