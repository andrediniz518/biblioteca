from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro
from .forms import LivroForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

def lista_livros(request):

    busca = request.GET.get('busca')
    livros = Livro.objects.all()
    if busca:
        livros = livros.filter(titulo__icontains=busca)

    paginator = Paginator(livros, 3)
    pagina = request.GET.get('pagina')
    livros = paginator.get_page(pagina)

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
            messages.success(request, 'Livro cadastrado com sucesso!')
            return redirect('lista_livros')
    else:
        form = LivroForm()
    return render(request, 'livros/cadastrar_livro.html', {'form': form})


def editar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)

        if form.is_valid():
            form.save()
            messages.success(request, 'Livro atualizado com sucesso!')
            return redirect('lista_livros')
    else:
        form = LivroForm(instance=livro)

    return render(request, 'livros/editar_livro.html', {'form': form})


def excluir_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    if request.method == 'POST':
        livro.delete()
        messages.success(request, 'Livro excluído com sucesso!')
        return redirect('lista_livros')
    return render(request, 'livros/excluir_livro.html', {'livro': livro})