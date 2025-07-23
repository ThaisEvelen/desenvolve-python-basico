import random
valor=random.randint(1,11)
n=int(input("Digite um valor entre 1 e 10: "))
while valor !=n:
    if valor>n:
        print("O número é menor que o valor digitado:")
    elif valor<n:
        print("O número é maior que o vaor digitado:")
n=int(input("Digite um valor entre 1 e 10: "))
print("Você acertou")