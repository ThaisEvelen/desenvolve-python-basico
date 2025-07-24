import random

# Gerar a lista com 20 números aleatórios entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]

print("Lista original:", lista)

# Variáveis para rastrear o maior intervalo de negativos
inicio = fim = 0
maior_inicio = maior_fim = -1
maior_tamanho = 0
i = 0

while i < len(lista):
    if lista[i] < 0:
        inicio = i
        while i < len(lista) and lista[i] < 0:
            i += 1
        fim = i  # índice final (exclusivo)
        tamanho = fim - inicio
        if tamanho > maior_tamanho:
            maior_tamanho = tamanho
            maior_inicio = inicio
            maior_fim = fim
    else:
        i += 1

# Exibir o intervalo encontrado (se existir)
if maior_tamanho > 0:
    print("Intervalo removido:", lista[maior_inicio:maior_fim])
    del lista[maior_inicio:maior_fim]
else:
    print("Nenhum intervalo de negativos encontrado.")

# Lista final
print("Lista final:", lista)
