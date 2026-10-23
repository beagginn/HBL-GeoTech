from django.shortcuts import render
from .models import Servico
from .models import Servico, ProjetoPortfolio
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ServicoForm, ProjetoPortfolioForm



# Create your views here.


def home(request):
    return render(request, "HBL/index.html")


def catalogo_servicos(request):
    servicos = Servico.objects.filter(ativo=True)

    return render(request, "HBL/catalogo.html", {
        "servicos": servicos,
    })


def portfolio(request):
    projetos = ProjetoPortfolio.objects.filter(ativo=True)

    return render(request, "HBL/portfolio.html", {
        "projetos": projetos,
    })

# DASHBOARD

@staff_member_required
def painel(request):
    contexto = {
        "total_servicos": Servico.objects.count(),
        "total_projetos": ProjetoPortfolio.objects.count(),
        "servicos_ativos": Servico.objects.filter(ativo=True).count(),
        "projetos_ativos": ProjetoPortfolio.objects.filter(ativo=True).count(),
        "ultimos_servicos": Servico.objects.order_by("-criado_em")[:5],
        "ultimos_projetos": ProjetoPortfolio.objects.order_by("-criado_em")[:5],
    }

    return render(request, "HBL/painel/dashboard.html", contexto)


# GERENCIAMENTO DE SERVIÇOS

@staff_member_required
def lista_servicos(request):
    servicos = Servico.objects.all()

    return render(request, "HBL/painel/servicos.html", {
        "servicos": servicos,
    })


@staff_member_required
def criar_servico(request):
    form = ServicoForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Serviço cadastrado com sucesso!")
        return redirect("painel_servicos")

    return render(request, "HBL/painel/form_servico.html", {
        "form": form,
        "titulo_pagina": "Adicionar serviço",
    })


@staff_member_required
def editar_servico(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    form = ServicoForm(
        request.POST or None,
        request.FILES or None,
        instance=servico,
    )

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Serviço atualizado com sucesso!")
        return redirect("painel_servicos")

    return render(request, "HBL/painel/form_servico.html", {
        "form": form,
        "titulo_pagina": "Editar serviço",
    })


@staff_member_required
def excluir_servico(request, pk):
    servico = get_object_or_404(Servico, pk=pk)

    if request.method == "POST":
        servico.delete()
        messages.success(request, "Serviço excluído com sucesso!")
        return redirect("painel_servicos")

    return render(request, "HBL/painel/confirmar_exclusao.html", {
        "objeto": servico,
        "tipo": "serviço",
        "voltar_url": "painel_servicos",
    })


# GERENCIAMENTO DE PROJETOS

@staff_member_required
def lista_projetos(request):
    projetos = ProjetoPortfolio.objects.all()

    return render(request, "HBL/painel/projetos.html", {
        "projetos": projetos,
    })


@staff_member_required
def criar_projeto(request):
    form = ProjetoPortfolioForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Projeto cadastrado com sucesso!")
        return redirect("painel_projetos")

    return render(request, "HBL/painel/form_projeto.html", {
        "form": form,
        "titulo_pagina": "Adicionar projeto",
    })


@staff_member_required
def editar_projeto(request, pk):
    projeto = get_object_or_404(ProjetoPortfolio, pk=pk)
    form = ProjetoPortfolioForm(
        request.POST or None,
        request.FILES or None,
        instance=projeto,
    )

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Projeto atualizado com sucesso!")
        return redirect("painel_projetos")

    return render(request, "HBL/painel/form_projeto.html", {
        "form": form,
        "titulo_pagina": "Editar projeto",
    })


@staff_member_required
def excluir_projeto(request, pk):
    projeto = get_object_or_404(ProjetoPortfolio, pk=pk)

    if request.method == "POST":
        projeto.delete()
        messages.success(request, "Projeto excluído com sucesso!")
        return redirect("painel_projetos")

    return render(request, "HBL/painel/confirmar_exclusao.html", {
        "objeto": projeto,
        "tipo": "projeto",
        "voltar_url": "painel_projetos",
    })
