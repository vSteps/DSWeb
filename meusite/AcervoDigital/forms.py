from django import forms
from .models import Livro, Contato
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class EmprestimoLivroForm(forms.ModelForm):
    contato = forms.ModelChoiceField(queryset=Contato.objects.all(), required=True, label="Contato")

    class Meta:
        model = Livro
        fields = ['contato']
        widgets = {
            'contato': forms.Select(attrs={'class': 'form-control'}),
        }

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de Usuário'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme a Senha'}),
        }

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['email', 'telefone']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
        }
