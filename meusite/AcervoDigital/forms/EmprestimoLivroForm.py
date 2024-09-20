class EmprestimoLivroForm(forms.ModelForm):
    contato = forms.ModelChoiceField(queryset=Contato.objects.all(), required=True, label="Contato")

    class Meta:
        model = Livro
        fields = ['contato']
        widgets = {
            'contato': forms.Select(attrs={'class': 'form-control'}),
        }
