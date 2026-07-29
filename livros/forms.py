from django import forms
from .models import Livro


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'ano_publicacao']

        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'autor': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'ano_publicacao': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
        }