from django.shortcuts import render
from utils.calendario.factory import make_calendario


def home(request):
    return render(request, 'calendario/pages/home.html', context={
        'calendario': [make_calendario()],
    })


def cadastro(request):
    return render(request, 'calendario/pages/cadastro.html', context={
        'calendario': make_calendario(),
    })


def calendario(request):
    return render(request, 'calendario/pages/calendario.html')
