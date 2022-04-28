from django.shortcuts import render


def home(request):
    return render(request, 'calendario/pages/home.html')


def cadastro(request):
    return render(request, 'calendario/pages/cadastro.html')


def calendario(request):
    return render(request, 'calendario/pages/calendario.html')
