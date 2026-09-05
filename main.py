from cadastro_tarefa import cadastrar_tarefa
from gerenciador_chamados import menu_chamados
from menu_tarefas import menu_tarefas
from tarefa import Tarefa
from servicos import cadastrar_tarefa as cadastrar_tarefa_objeto


# Lista de tarefas da Atividade 5
tarefas = []


# Cadastra 3 tarefas para demonstrar o funcionamento
cadastrar_tarefa_objeto(
    tarefas,
    "Revisar chamados",
    "Verificar chamados pendentes da equipe",
    "Alta",
    Tarefa
)

cadastrar_tarefa_objeto(
    tarefas,
    "Atualizar manual interno",
    "Ajustar instruções de atendimento",
    "Média",
    Tarefa
)

cadastrar_tarefa_objeto(
    tarefas,
    "Planejar reunião",
    "Preparar pauta da reunião semanal",
    "Baixa",
    Tarefa
)


# Conclui a primeira tarefa
tarefas[0].concluir()


# Menu principal
while True:
    print("\n========================================")
    print("       SISTEMA DE CONTROLE INTERNO")
    print("========================================")
    print("1 - Cadastro de tarefa")
    print("2 - Gerenciador de chamados")
    print("3 - Gerenciador de tarefas")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        cadastrar_tarefa()

    elif opcao == "2":
        menu_chamados()

    elif opcao == "3":
        menu_tarefas(tarefas)

    elif opcao == "4":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida. Escolha de 1 a 4.")