
lista1 = list(map(int, input("Digite os números da primeira lista, separados por espaço: ").split()))
lista2 = list(map(int, input("Digite os números da segunda lista, separados por espaço: ").split()))

lista_intercalada = []

menor_tamanho = min(len(lista1), len(lista2))

for i in range(menor_tamanho):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])

if len(lista1) > len(lista2):
    lista_intercalada.extend(lista1[menor_tamanho:])
else:
    lista_intercalada.extend(lista2[menor_tamanho:])
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista Intercalada:", lista_intercalada)
