class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['nome', 'autor', 'ano', 'imagem']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Livro'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Autor'}),
            'ano': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Data de Publicação'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
