tarefas = []

def imprimir():
    print("\nLista de tarefas:")

    for indice,tarefa in enumerate(tarefas):
        print(indice + 1, "-", tarefa)

while True:
    nova_tarefa = input("Digite uma tarefa:")
   
    if nova_tarefa == "sair":
        break

    elif nova_tarefa == "exibir":
        imprimir()

    elif nova_tarefa == "remover":
        imprimir()
        
        numero = input("Digite o número da tarefa para remover:")
        numero = int(numero)
       
        tarefas.pop(numero - 1)

    else:
        tarefas.append(nova_tarefa)
