import json
import os

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)



def adicionar_tarefa(tarefas):
    titulo = input("Digite o nome da tarefa: ")

    tarefa = {
        "titulo": titulo,
        "concluida": False
    }

    tarefas.append(tarefa)

    salvar_tarefas(tarefas)

    print("✅ Tarefa adicionada com sucesso!")



def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\n📋 LISTA DE TAREFAS:\n")

    for i, tarefa in enumerate(tarefas, start=1):
        status = "✔️" if tarefa["concluida"] else "❌"
        print(f"{i} - {tarefa['titulo']} [{status}]")



def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)

    try:
        indice = int(input("Digite o número da tarefa para concluir: ")) - 1

        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True

            salvar_tarefas(tarefas)

            print("🎉 Tarefa concluída!")
        else:
            print("Número inválido.")

    except ValueError:
        print("Digite um número válido.")



def remover_tarefa(tarefas):
    listar_tarefas(tarefas)

    try:
        indice = int(input("Digite o número da tarefa para remover: ")) - 1

        if 0 <= indice < len(tarefas):
            tarefa_removida = tarefas.pop(indice)

            salvar_tarefas(tarefas)

            print(f"🗑️ Tarefa '{tarefa_removida['titulo']}' removida.")
        else:
            print("Número inválido.")

    except ValueError:
        print("Digite um número válido.")



def menu():
    tarefas = carregar_tarefas()

    while True:
        print("\n====== TO-DO LIST ======")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)

        elif opcao == "2":
            listar_tarefas(tarefas)

        elif opcao == "3":
            concluir_tarefa(tarefas)

        elif opcao == "4":
            remover_tarefa(tarefas)

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")



if __name__ == "__main__":
    menu()