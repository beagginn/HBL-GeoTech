from django.db import models

# Create your models here.

class Servico(models.Model):
    nome = models.CharField(
        max_length=150,
        verbose_name="Nome do serviço"
    )

    descricao = models.TextField(
        verbose_name="Descrição"
    )

    imagem = models.ImageField(
        upload_to="servicos/",
        blank=True,
        null=True,
        verbose_name="Imagem do serviço"
    )

    ativo = models.BooleanField(
        default=True,
        verbose_name="Exibir no catálogo"
    )

    ordem = models.PositiveIntegerField(
        default=0,
        verbose_name="Ordem de exibição"
    )

    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["ordem", "nome"]
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

    def __str__(self):
        return self.nome

class ProjetoPortfolio(models.Model):
    titulo = models.CharField(
        max_length=150,
        verbose_name="Título do projeto"
    )

    descricao = models.TextField(
        verbose_name="Descrição"
    )

    imagem = models.ImageField(
        upload_to="portfolio/",
        verbose_name="Imagem do projeto"
    )

    categoria = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Categoria"
    )

    local = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Local do projeto"
    )

    ano = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Ano do projeto"
    )

    link = models.URLField(
        blank=True,
        verbose_name="Link externo"
    )

    ativo = models.BooleanField(
        default=True,
        verbose_name="Exibir no portfólio"
    )

    ordem = models.PositiveIntegerField(
        default=0,
        verbose_name="Ordem de exibição"
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["ordem", "-criado_em"]
        verbose_name = "Projeto do portfólio"
        verbose_name_plural = "Projetos do portfólio"

    def __str__(self):
        return self.titulo