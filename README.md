# 📚 Sistema de Gerenciamento de Biblioteca

Projeto desenvolvido com Django para praticar a construção de uma aplicação web completa utilizando operações CRUD, autenticação de usuários e organização de dados.

## 🌐 Projeto publicado

Acesse a aplicação:

https://biblioteca-qzux.onrender.com/livros/

---

## 🚀 Tecnologias utilizadas

* Python
* Django
* HTML5
* Bootstrap 5
* SQLite
* Gunicorn
* Render

---

## 📌 Funcionalidades

* Cadastro de livros
* Listagem de livros
* Visualização dos detalhes de um livro
* Edição de livros cadastrados
* Exclusão de livros
* Cadastro e gerenciamento pelo Django Admin
* Mensagens de sucesso após operações
* Paginação dos livros
* Busca de livros por título
* Sistema de login e logout
* Controle de acesso para usuários autenticados
* Interface responsiva utilizando Bootstrap

---

## 🖼️ Demonstração

A aplicação permite gerenciar uma biblioteca de livros através de uma interface simples e organizada.

Principais telas:

* Lista de livros
* Cadastro de livros
* Edição de livros
* Detalhes do livro
* Login de usuários
* Painel administrativo Django

---

## 📂 Estrutura do projeto

```
biblioteca/
│
├── biblioteca/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── livros/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── templates/
│
├── manage.py
├── requirements.txt
└── Procfile
```

---

## ⚙️ Como executar localmente

### 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Acesse a pasta do projeto

```bash
cd biblioteca
```

### 3. Crie um ambiente virtual

```bash
python -m venv venv
```

### 4. Ative o ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Execute as migrations

```bash
python manage.py migrate
```

### 7. Inicie o servidor

```bash
python manage.py runserver
```

Acesse:

```
http://127.0.0.1:8000/livros/
```

---

## 🔐 Usuário administrador

Para criar um usuário administrador:

```bash
python manage.py createsuperuser
```

Acesse:

```
http://127.0.0.1:8000/admin/
```

---

## ☁️ Deploy

O projeto foi publicado utilizando:

* Render
* Gunicorn

Configurações de produção aplicadas:

* `DEBUG=False`
* `ALLOWED_HOSTS`
* `collectstatic`
* `requirements.txt`
* `Procfile`

---

## 📚 Objetivo do projeto

Este projeto foi desenvolvido com o objetivo de consolidar conhecimentos em Django, principalmente:

* Modelagem de dados
* Views e Templates
* Formulários
* CRUD completo
* Autenticação
* ORM do Django
* Deploy de aplicações web
