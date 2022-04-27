from django.urls import path
from calendario.views import cadastro, calendario, home

urlpatterns = [
    path('', home),
    path('cadastro/', cadastro),
    path('calendario/', calendario),
]
