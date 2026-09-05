from django.shortcuts import render, redirect


tarefas = [
    {
        "titulo": "Estudar Django",
        "prioridade": "Alta",
        "situacao": "Pendente",
    },
    {
        "titulo": "Criar página HTML",
        "prioridade": "Média",
        "situacao": "Concluída",
    },
]


def inicio(request):
    return render(request, "tarefas/inicio.html")


def lista_tarefas(request):
    return render(
        request,
        "tarefas/lista.html",
        {"tarefas": tarefas}
    )


def cadastrar_tarefa(request):

    if request.method == "POST":

        titulo = request.POST.get("titulo")
        prioridade = request.POST.get("prioridade")
        situacao = request.POST.get("situacao")

        if titulo:
            tarefas.append({
                "titulo": titulo,
                "prioridade": prioridade,
                "situacao": situacao,
            })

        return redirect("lista_tarefas")

    return render(request, "tarefas/cadastrar.html")