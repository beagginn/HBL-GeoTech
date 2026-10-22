
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
        path("servicos/", views.catalogo_servicos, name="catalogo_servicos"
    ),
]