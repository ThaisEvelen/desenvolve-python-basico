import random

aleatorios=[]
for i in range(20):
    valor= random.randint(-100,100)
    aleatorios.append(valor)
print(sorted(aleatorios))
print(aleatorios)
print("O maior valor esta no índice: ",aleatorios.index(max(aleatorios)))
print("O menor valor está no índice : ", aleatorios.index(min(aleatorios)))