from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("tarefas/", views.lista_tarefas, name="lista_tarefas"),
    path("cadastrar/", views.cadastrar_tarefa, name="cadastrar_tarefa"),
]