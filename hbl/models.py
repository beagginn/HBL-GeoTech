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