from django.shortcuts import render
from .models import Livro


# Create your views here.

def lista_livros(request):
    livros = Livro.objects.all()

    contexto = {
        'livros': livros
    }

    return render(request, 'livros/lista_livros.html', contexto)