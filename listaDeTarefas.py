from InquirerPy import prompt
import os


# Função principal do programa

def listaDeTarefas():
    # Inicializa uma lista vazia para armazenar as tarefas
    tarefas = []

    # Função para exibir a lista de tarefas
    def exibir_tarefas():
        if not tarefas:
            print("A lista de tarefas está vazia.")
        else:
            print("\nTarefas:")
            for i, tarefa in enumerate(tarefas, start=1):
                status = "Concluída" if tarefa["concluida"] else "Pendente"
                print(f"{i}. {tarefa['nome']} - {status}")
        input("\nPressione Enter para continuar...")  # Aguarda o usuário pressionar Enter

    # Função para adicionar uma nova tarefa
    def adicionar_tarefa():
        while True:
            tarefa = input("Digite a nova tarefa: ")
            if tarefa:
                tarefas.append({"nome": tarefa, "concluida": False})
                print(f"Tarefa '{tarefa}' adicionada com sucesso e marcada como Pendente.")
                input("\nPressione Enter para continuar...")  # Aguarda o usuário pressionar Enter
                break
            else:
                print("Ocorreu um erro ao adicionar a tarefa.")
                print("Entrada inválida. Por favor, tente novamente.")
                input("\nPressione Enter para continuar...")  # Aguarda o usuário pressionar Enter

    # Função para remover uma tarefa
    def remover_tarefa():
        if not tarefas:
            print("A lista de tarefas está vazia.")
            input("\nPressione Enter para continuar...")  # Aguarda o usuário pressionar Enter
            return

        # Lista de opções para InquirerPy
        opcoes_tarefas = [
            {"name": f"{tarefa['nome']} - {'Concluída' if tarefa['concluida'] else 'Pendente'}", "value": i}
            for i, tarefa in enumerate(tarefas)]

        opcoes_remover = [
            {
                "type": "list",
                "message": "Selecione a tarefa que deseja remover:",
                "name": "tarefa",
                "choices": opcoes_tarefas
            }
        ]

        resposta = prompt(opcoes_remover)
        indice_tarefa = resposta.get("tarefa")

        if indice_tarefa is not None:
            tarefa_removida = tarefas.pop(indice_tarefa)
            print(f"Tarefa '{tarefa_removida['nome']}' removida com sucesso!")
        input("\nPressione Enter para continuar...")  # Aguarda o usuário pressionar Enter

    # Função para marcar uma tarefa como concluída
    def concluir_tarefa():
        if not tarefas:
            print("A lista de tarefas está vazia.")
            input("\nPressione Enter para continuar...")  # Aguarda o usuário pressionar Enter
            return

        # Lista de opções para InquirerPy
        opcoes_tarefas = [
            {"name": f"{tarefa['nome']} - {'Concluída' if tarefa['concluida'] else 'Pendente'}", "value": i}
            for i, tarefa in enumerate(tarefas) if not tarefa["concluida"]]

        if not opcoes_tarefas:
            print("Não há tarefas pendentes para marcar como concluídas.")
            input("\nPressione Enter para continuar...")
            return

        opcoes_concluir = [
            {
                "type": "list",
                "message": "Selecione a tarefa que deseja marcar como concluída:",
                "name": "tarefa",
                "choices": opcoes_tarefas
            }
        ]

        resposta = prompt(opcoes_concluir)
        indice_tarefa = resposta.get("tarefa")

        if indice_tarefa is not None:
            tarefas[indice_tarefa]["concluida"] = True
            print(f"Tarefa '{tarefas[indice_tarefa]['nome']}' marcada como Concluída!")
        input("\nPressione Enter para continuar...")  # Aguarda o usuário pressionar Enter

    # Função para limpar todas as tarefas da lista
    def limpar_tarefas():
        if not tarefas:
            print("A lista de tarefas está vazia.")
        else:
            confirmacao = input("Tem certeza de que deseja limpar todas as tarefas? (s/n): ")
            if confirmacao.lower() == 's':
                tarefas.clear()
                print("Todas as tarefas foram removidas com sucesso!")
            else:
                print("Operação de limpeza cancelada.")
        input("\nPressione Enter para continuar...")  # Aguarda o usuário pressionar Enter

    # Função principal para o menu
    def menu():
        while True:
            opcoesMenu = [
                {
                    "type": "list",
                    "message": "Menu de opções:",
                    "name": "opcao",
                    "choices": ["Exibir Tarefas", "Adicionar Tarefa", "Remover Tarefa", "Concluir Tarefa",
                                "Limpar Todas as Tarefas", "Sair"]
                },
            ]

            os.system("cls")
            respostaMenu = prompt(opcoesMenu)
            opcaoMenu = respostaMenu.get("opcao")  # Acessa a escolha do usuário

            if opcaoMenu == "Exibir Tarefas":
                exibir_tarefas()
            elif opcaoMenu == "Adicionar Tarefa":
                adicionar_tarefa()
            elif opcaoMenu == "Remover Tarefa":
                remover_tarefa()
            elif opcaoMenu == "Concluir Tarefa":
                concluir_tarefa()
            elif opcaoMenu == "Limpar Todas as Tarefas":
                limpar_tarefas()
            elif opcaoMenu == "Sair":
                print("Saindo do programa...")
                break

    # Executa o menu da lista de tarefas
    menu()


# Executa a lista de tarefas

listaDeTarefas()
