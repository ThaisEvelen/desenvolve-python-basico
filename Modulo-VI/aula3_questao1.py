
entrada = input("Digite pelo menos 4 números inteiros separados por espaço: ").split()
lista = [int(num) for num in entrada]

if len(lista) < 4:
    print("Erro: É necessário digitar pelo menos 4 números.")
else:
    print("\nLista original:", lista)
    print("Os 3 primeiros elementos:", lista[:3])
    print("Os 2 últimos elementos:", lista[-2:])
    print("Lista invertida:", lista[::-1])
    print("Elementos de índice par:", lista[0::2])
    print("Elementos de índice ímpar:", lista[1::2])
