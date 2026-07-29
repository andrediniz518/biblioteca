from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_livros, name='lista_livros'),
    path('<int:id>/', views.detalhe_livro, name='detalhe_livro'),
    path('cadastrar/', views.cadastrar_livro, name='cadastrar_livro'),
]