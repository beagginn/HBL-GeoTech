
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("servicos/", views.catalogo_servicos, name="catalogo_servicos"),
    path("portfolio/", views.portfolio, name="portfolio"),

    # Dashboard
    path("painel/", views.painel, name="painel"),

    # Serviços
    path("painel/servicos/", views.lista_servicos, name="painel_servicos"),
    path("painel/servicos/adicionar/", views.criar_servico, name="criar_servico"),
    path("painel/servicos/<int:pk>/editar/", views.editar_servico, name="editar_servico"),
    path("painel/servicos/<int:pk>/excluir/", views.excluir_servico, name="excluir_servico"),

    # Projetos
    path("painel/projetos/", views.lista_projetos, name="painel_projetos"),
    path("painel/projetos/adicionar/", views.criar_projeto, name="criar_projeto"),
    path("painel/projetos/<int:pk>/editar/", views.editar_projeto, name="editar_projeto"),
    path("painel/projetos/<int:pk>/excluir/", views.excluir_projeto, name="excluir_projeto"),
]