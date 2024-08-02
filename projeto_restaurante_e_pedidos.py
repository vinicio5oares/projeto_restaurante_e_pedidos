# listas
cliente=[]
pedidos=[]
restaurante=[]
# adicionar restaurante
def adicionar_restaurante(nome_do_restaurante):
    restaurante.append(nome_do_restaurante)
# adicionar pedido
def adicionar_pedido(nome_do_cliente,pedido):
    cliente.append(nome_do_cliente)
    pedidos.append(pedido)
# listar pedido
def listar_pedidos():
    for i in range(len(pedidos)):
        print("restaurante: ",restaurante[i], "Nome: ", cliente[i], "Pedido: " ,pedidos[i])
# atualizar pedido
def atualizar_pedido():
    nome_cliente = input("Digite o nome do cliente que deseja atualizar o pedido:")
    if cliente in nome_cliente:
        pedido = input("Digite o novo pedido:")
        pedidos[nome_cliente] = pedido
    else:
        print("Cliente não encontrado")
# excluir pedido
def excluir_pedido():
    nome_cliente = input("Digite o nome do cliente que deseja excluir o pedido:")
    if cliente in nome_cliente:
        pedidos.remove(nome_cliente)
    else:
        print("Cliente não encontrado")
# menu
while True:
    print("1 - Adicionar pedido")
    print("2 - Listar pedido")
    print("3 - Atualizar pedido")
    print("4 - Excluir pedido")
    print("5 - Sair")

    opcao = int(input("Digite a opção desejada:"))
    if opcao == 1:
        nome_do_restaurante=input("Digite o nome do restaurante: ")
        adicionar_restaurante(nome_do_restaurante)

        nome_do_cliente = input("Digite o nome do cliente:")
        pedido = input("Digite o pedido:")
        adicionar_pedido(nome_do_cliente,pedido)
    elif opcao == 2:
        listar_pedidos()
    elif opcao == 3:
        atualizar_pedido()
    elif opcao == 4:
        excluir_pedido()
    elif opcao == 5:
        print("encerrando, OBRIGADO!")
        break
    else:
        print("Opção inválida, tente novamente")