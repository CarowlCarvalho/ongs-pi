from django.shortcuts import render


def index(request):
    return render(request, 'galeria/index.html')

def cadastro(request):
    return render(request, 'galeria/cadastro.html')

def login(request):
    return render(request, 'galeria/login.html')

def participa(request):
    return render(request, 'galeria/quemparticipa.html')

def artigos(request):
    return render(request, 'galeria/artigos.html')

def perfil(request):
    return render(request, 'galeria/perfil.html')