
from django import forms
from .models import Servico, ProjetoPortfolio


class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ["nome", "descricao", "imagem", "ativo", "ordem"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "descricao": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
            }),
            "imagem": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "ativo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "ordem": forms.NumberInput(attrs={"class": "form-control"}),
        }


class ProjetoPortfolioForm(forms.ModelForm):
    class Meta:
        model = ProjetoPortfolio
        fields = [
            "titulo",
            "descricao",
            "imagem",
            "categoria",
            "local",
            "ano",
            "link",
            "ativo",
            "ordem",
        ]
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "descricao": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
            }),
            "imagem": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "categoria": forms.TextInput(attrs={"class": "form-control"}),
            "local": forms.TextInput(attrs={"class": "form-control"}),
            "ano": forms.NumberInput(attrs={"class": "form-control"}),
            "link": forms.URLInput(attrs={"class": "form-control"}),
            "ativo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "ordem": forms.NumberInput(attrs={"class": "form-control"}),
        }
