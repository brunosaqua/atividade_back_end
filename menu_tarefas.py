from tarefa import Tarefa
from servicos import cadastrar_tarefa, listar_tarefas, filtrar_por_situacao


def menu_tarefas(tarefas):
    while True:
        print("\n===== MENU DE TAREFAS =====")
        print("1 - Cadastrar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Listar concluídas")
        print("5 - Listar pendentes")
        print("6 - Voltar ao menu principal")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            titulo = input("Digite o título: ").strip()
            descricao = input("Digite a descrição: ").strip()
            prioridade = input(
                "Digite a prioridade (baixa, média ou alta): "
            ).strip().capitalize()

            if titulo == "":
                print("O título não pode estar vazio.")

            elif prioridade not in ["Baixa", "Média", "Alta"]:
                print("Prioridade inválida.")

            else:
                cadastrar_tarefa(
                    tarefas,
                    titulo,
                    descricao,
                    prioridade,
                    Tarefa
                )

                print("Tarefa cadastrada com sucesso!")

        elif opcao == "2":
            print("\n===== TODAS AS TAREFAS =====")
            listar_tarefas(tarefas)

        elif opcao == "3":
            if not tarefas:
                print("Não há tarefas cadastradas.")
            else:
                numero = input(
                    "Digite o número da tarefa que deseja concluir: "
                ).strip()

                if numero.isdigit():
                    indice = int(numero) - 1

                    if 0 <= indice < len(tarefas):
                        tarefas[indice].concluir()
                        print("Tarefa concluída com sucesso!")
                    else:
                        print("Tarefa inexistente.")
                else:
                    print("Digite apenas o número da tarefa.")

        elif opcao == "4":
            print("\n===== TAREFAS CONCLUÍDAS =====")
            tarefas_concluidas = filtrar_por_situacao(
                tarefas, "Concluída"
            )
            listar_tarefas(tarefas_concluidas)

        elif opcao == "5":
            print("\n===== TAREFAS PENDENTES =====")
            tarefas_pendentes = filtrar_por_situacao(
                tarefas, "Pendente"
            )
            listar_tarefas(tarefas_pendentes)

        elif opcao == "6":
            print("Voltando ao menu principal...")
            break

        else:
            print("Opção inválida.")