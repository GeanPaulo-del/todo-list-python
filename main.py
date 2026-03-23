import json

def carregar_tarefas():
    try:
        with open("tarefas.json", "r") as arquivo:
            return json.load(arquivo)
    except:
        return []

def salvar_tarefas():
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo)

tarefas = carregar_tarefas()

def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ")
    tarefas.append({"tarefa": tarefa, "concluida": False})
    salvar_tarefas()
    print("Tarefa adicionada!")

def ver_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for i, t in enumerate(tarefas):
        status = "✔" if t["concluida"] else "❌"
        print(f"{i + 1}. {t['tarefa']} [{status}]")

def concluir_tarefa():
    ver_tarefas()

    try:
        numero = int(input("Número da tarefa para concluir: "))
        tarefas[numero - 1]["concluida"] = True
        salvar_tarefas()
        print("Tarefa concluída!")
    except:
        print("Erro ao concluir tarefa.")

def remover_tarefa():
    ver_tarefas()

    try:
        numero = int(input("Número da tarefa para remover: "))
        tarefas.pop(numero - 1)
        salvar_tarefas()
        print("Tarefa removida!")
    except:
        print("Erro ao remover tarefa.")

while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        adicionar_tarefa()

    elif opcao == "2":
        ver_tarefas()

    elif opcao == "3":
        concluir_tarefa()

    elif opcao == "4":
        remover_tarefa()

    elif opcao == "5":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
