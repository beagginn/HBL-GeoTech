from django.contrib import admin

# Register your models here.

from .models import Servico


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