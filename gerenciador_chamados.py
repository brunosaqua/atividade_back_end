# Gerenciador de Chamados Internos

chamados = [
    {
        "id": 1,
        "titulo": "Sem acesso ao sistema interno",
        "prioridade": "alta",
        "situacao": "aberto",
        "categoria": "acesso"
    },
    {
        "id": 2,
        "titulo": "Impressora sem conexão",
        "prioridade": "média",
        "situacao": "em atendimento",
        "categoria": "hardware"
    },
    {
        "id": 3,
        "titulo": "Erro ao acessar o e-mail",
        "prioridade": "alta",
        "situacao": "aberto",
        "categoria": "acesso"
    },
    {
        "id": 4,
        "titulo": "Computador muito lento",
        "prioridade": "baixa",
        "situacao": "resolvido",
        "categoria": "hardware"
    },
    {
        "id": 5,
        "titulo": "Instalação de novo software",
        "prioridade": "média",
        "situacao": "em atendimento",
        "categoria": "software"
    }
]


def listar_chamados():
    print("========================================")
    print("       TODOS OS CHAMADOS")
    print("========================================")

    for chamado in chamados:
        print(f"ID: {chamado['id']}")
        print(f"Título: {chamado['titulo']}")
        print(f"Prioridade: {chamado['prioridade']}")
        print(f"Situação: {chamado['situacao']}")
        print(f"Categoria: {chamado['categoria']}")
        print("----------------------------------------")


def filtrar_por_situacao(situacao_desejada):
    encontrou = False

    print("\n========================================")
    print(f"CHAMADOS COM SITUAÇÃO: {situacao_desejada}")
    print("========================================")

    for chamado in chamados:
        if chamado["situacao"] == situacao_desejada:
            encontrou = True
            print(f"ID: {chamado['id']}")
            print(f"Título: {chamado['titulo']}")
            print(f"Prioridade: {chamado['prioridade']}")
            print(f"Categoria: {chamado['categoria']}")
            print("----------------------------------------")

    if not encontrou:
        print("Nenhum chamado encontrado nessa situação.")


def atualizar_chamado(id_desejado, nova_situacao):
    for chamado in chamados:
        if chamado["id"] == id_desejado:
            chamado["situacao"] = nova_situacao
            print(f"Chamado {id_desejado} atualizado com sucesso!")
            print(f"Nova situação: {nova_situacao}")
            return True

    print("Chamado não encontrado.")
    return False


def listar_categorias():
    categorias = set()

    for chamado in chamados:
        categorias.add(chamado["categoria"])

    print("\n========================================")
    print("       CATEGORIAS DOS CHAMADOS")
    print("========================================")

    for categoria in categorias:
        print(f"- {categoria}")


def menu_chamados():
    while True:
        print("\n===== GERENCIADOR DE CHAMADOS =====")
        print("1 - Listar chamados")
        print("2 - Filtrar por situação")
        print("3 - Atualizar chamado")
        print("4 - Listar categorias")
        print("5 - Voltar ao menu principal")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_chamados()

        elif opcao == "2":
            situacao = input(
                "Digite a situação (aberto, em atendimento, resolvido): "
            ).strip().lower()

            filtrar_por_situacao(situacao)

        elif opcao == "3":
            id_desejado = input("Digite o ID do chamado: ").strip()
            nova_situacao = input(
                "Digite a nova situação: "
            ).strip().lower()

            if id_desejado.isdigit():
                atualizar_chamado(
                    int(id_desejado),
                    nova_situacao
                )
            else:
                print("Digite um ID válido.")

        elif opcao == "4":
            listar_categorias()

        elif opcao == "5":
            break

        else:
            print("Opção inválida.")