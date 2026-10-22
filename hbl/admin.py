from django.contrib import admin

# Register your models here.

from .models import Servico
from .models import Servico, ProjetoPortfolio


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "ativo",
        "ordem",
        "criado_em",
    )

    list_filter = ("ativo",)

    search_fields = (
        "nome",
        "descricao",
    )

    list_editable = (
        "ativo",
        "ordem",
    )

    ordering = ("ordem", "nome")


@admin.register(ProjetoPortfolio)
class ProjetoPortfolioAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "categoria",
        "local",
        "ano",
        "ativo",
        "ordem",
    )

    list_filter = (
        "ativo",
        "categoria",
        "ano",
    )

    search_fields = (
        "titulo",
        "descricao",
        "categoria",
        "local",
    )

    list_editable = (
        "ativo",
        "ordem",
    )

    ordering = (
        "ordem",
        "-criado_em",
    )