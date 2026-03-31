lista = []

def cadastrarUsuario(lista):
    nome = input("Digite o nome :")
    lista.append(nome)

def imprimirLista(lista):
    print("Seus usuarios sao: ")
    for indice, nome in enumerate(lista):
        print(indice, ' - ', nome)

while True:
    print("------ ")
    print("Digite uma opca: ")
    print( 1, "cadastrar usuario")
    print( 2, "remover usuario")
    print( 4, "imprimir lista")
    print(5, "sair")
    opcao  = input("Digite uma opcao :")

    if opcao == "1":
        cadastrarUsuario(lista)
        

    if opcao == "4":
        imprimirLista(lista)




print("\nLista atual:")



