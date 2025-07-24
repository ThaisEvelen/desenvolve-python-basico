import random

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

interseccao = list(set(lista1) & set(lista2))  
interseccao.sort()

print("Lista 1:", sorted(lista1))
print("Lista 2:", sorted(lista2))

print("Interseção:", interseccao)

print("\nContagem de aparições:")
for elemento in interseccao:
    print(f"{elemento}: ({lista1.count(elemento)}, {lista2.count(elemento)})")
