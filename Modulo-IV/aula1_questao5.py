n = int(input("Digite a quantidade de respondentes: "))
soma = 0
contador = n 

while n > 0:
    idade = int(input("Digite a idade do respondente: "))
    soma += idade
    n -= 1

media = soma / contador
print("A média das idades é:", media)
