import random
valor=random.randint(1,10)
n=int(input("Digite um valor entre 1 e 10: "))
while valor !=n:
    if valor>n:
        print("O número é maior que o valor digitado:")
    elif valor<n:
        print("O número é menor que o valor digitado:")
    n=int(input("Digite novamente um valor:"))
print("Você acertou")