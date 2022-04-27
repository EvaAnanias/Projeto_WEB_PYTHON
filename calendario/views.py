from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'calendario/home.html')


def cadastro(request):
    return HttpResponse('Tela de Cadastro')


def calendario(request):
    return HttpResponse('Tela do Calendario')
