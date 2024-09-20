class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['email', 'telefone']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
        }