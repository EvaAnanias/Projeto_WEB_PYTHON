from django.shortcuts import render


def home(request):
    return render(request, 'calendario/home.html')


def cadastro(request):
    return render(request, 'calendario/cadastro.html')


def calendario(request):
    return render(request, 'calendario/calendario.html')
