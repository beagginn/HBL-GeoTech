from django.shortcuts import render
from .models import Servico


# Create your views here.


def home(request):
    return render(request, "hbl/index.html")


def catalogo_servicos(request):
    servicos = Servico.objects.filter(ativo=True)

    return render(request, "hbl/catalogo.html", {
        "servicos": servicos,
    })