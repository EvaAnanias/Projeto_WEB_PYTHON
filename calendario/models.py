from django import forms
from django.db import models

# Create your models here.


# class Category(models.Model):  nome = models.CharField(max_length=65)


class calendarioForm(forms.Form):

    nome = forms.CharField(
        label='nome_compromisso',
        max_length=65)

    nome = forms.DateTimeField(
        label='data_compromisso',
        auto_now_add=True)

    nome = forms.CharField(
        label='nome_compromisso',
        max_length=65)

    nome = forms.CharField(
        label='nome_compromisso',
        max_length=65)

    nome = forms.CharField(
        label='nome_compromisso',
        max_length=65)

    nome = forms.CharField(
        label='nome_compromisso',
        max_length=65)

    # category = models.ForeignKey(
    #   Category, on_delete=models.SET_NULL, null=True
    # )
    # author = models.ForeignKey(
    #    Category, on_delete=models.SET_NULL, null=True
    # )


class calendario(models.Model):
    nome_compromisso = models.CharField(max_length=65)
    data_compromisso = models.DateTimeField(auto_now_add=True)
    local = models.CharField(max_length=80)
    hora_inicio = models.IntegerField()
    hora_termino = models.IntegerField()
    message = models.TextField(blank=True, null=True)
