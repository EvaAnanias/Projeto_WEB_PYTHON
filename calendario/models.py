from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    nome = models.CharField(max_length=65)


class Calendario(models.Model):
    nome = models.CharField(max_length=65)
    data = models.DateTimeField(auto_now_add=True)
    local = models.CharField(max_length=80)
    hora_inicio = models.IntegerField()
    hora_termino = models.IntegerField()
    observação = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    author = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
