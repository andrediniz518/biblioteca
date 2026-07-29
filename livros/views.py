from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro
from .forms import LivroForm


# Create your views here.

def lista_livros(request):
    livros = Livro.objects.all()
    contexto = {
        'livros': livros
    }
    return render(request, 'livros/lista_livros.html', contexto)


def detalhe_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    contexto = {
        'livro': livro

    }
    return render(request, 'livros/detalhe_livro.html', contexto)


def cadastrar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = LivroForm()
    return render(request, 'livros/cadastrar_livro.html', {'form': form})
