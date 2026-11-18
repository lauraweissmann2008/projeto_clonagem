
#Crie um programa com o seguinte menu:
#1 - Adicionar item à lista
#2 - Remover item pelo índice
#3 - Verificar se um item está na lista
#4 - Mostrar todos os itens
#5 - Ordenar lista
#6 - Sair
#O programa deve:
#Começar com uma lista vazia.
#Permitir que o usuário insira a quantidade de itens sempre que necessário.
#Utilizar um controle de menu.
#Capturar entradas inválidas

lista_itens = []

while True:
    print("\n========= MENU =========")
    print("1 - Adicionar item à lista")
    print("2 - Remover item pelo índice")
    print("3 - Verificar se um item está na lista")
    print("4 - Mostrar todos os itens")
    print("5 - Ordenar lista")
    print("6 - Sair")
    print("========================")
    
    opcao = int(input("Escolha uma opção (1-6): "))

    if opcao == 1:
        qtd = int(input("Quantos itens deseja adicionar? "))
        for i in range(qtd):
            item = input(f"Digite o {i+1}º item: ")
            lista_itens.append(item)
        print("Item(ns) adicionado(s)!")

    elif opcao == 2:
        if len(lista_itens) == 0:
            print("A lista está vazia!")
        else:
            print(f"Lista atual: {lista_itens}")
            indice = int(input("Digite o índice que deseja remover: "))
            
            if 0 <= indice < len(lista_itens):
                item_removido = lista_itens.pop(indice)
                print(f"Item '{item_removido}' removido!")
            else:
                print("Índice inválido!")
    elif opcao == 3:
        item_pesquisa = input("Digite o nome do item: ")
        if item_pesquisa in lista_itens:
            print(f"O item '{item_pesquisa}' ESTÁ na lista!")
        else:
            print(f"O item '{item_pesquisa}' NÃO está na lista.")

    elif opcao == 4:
        if len(lista_itens) == 0:
            print("A lista está vazia.")
        else:
            print(f"Itens na lista: {lista_itens}")

    elif opcao == 5:
        lista_itens.sort()
        print(f"Lista ordenada: {lista_itens}")

    elif opcao == 6:
        print("Saindo...")
        break

    else:
        print("Opção inválida!")