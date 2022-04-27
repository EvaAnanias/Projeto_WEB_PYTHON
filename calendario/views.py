from django.http import HttpResponse

# from django.shortcuts import render


def home(request):
    return HttpResponse('Home 1')


def cadastro(request):
    return HttpResponse('Tela de Cadastro')


def calendario(request):
    return HttpResponse('Tela do Calendario')
