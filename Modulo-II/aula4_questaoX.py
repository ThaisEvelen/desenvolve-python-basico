#Questão 1
comprimento= int(input("Digite o comprimento do terreno:"))
largura= int(input("Digite a largura do terreno:"))
preco_m2 = float(input("Digite o preço do metro quadrado: "))
area_m2=(comprimento*largura)
print(area_m2)
preco_total = preco_m2 * area_m2
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")

#Questão 2
fahrenheit = int(input("Digite a temperatura em graus Fahrenheit: "))
celsius = (fahrenheit - 32) * (5 / 9)
celsius = int(celsius)
print(f"{fahrenheit} graus Fahrenheit são {celsius} graus Celsius.")

#Questão 3
produto1 = input("Digite o nome do produto 1:")
preco1 = float(input("Digite o preço unitário do produto 1:"))
qtd1 = int(input("Digite a quantidade do produto 1:"))

produto2 = input("Digite o nome do produto 2:")
preco2 = float(input("Digite o preço unitário do produto 2:"))
qtd2 = int(input("Digite a quantidade do produto 2:"))

produto3 = input("Digite o nome do produto 3:")
preco3 = float(input("Digite o preço unitário do produto 3:"))
qtd3 = int(input("Digite a quantidade do produto 3:"))

total = (preco1 * qtd1) + (preco2 * qtd2) + (preco3 * qtd3)
total_formatado = f"{total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
print(f"Total: R${total_formatado}")

#Questão 4
valor = int(input("Digite o valor:"))

n100 = valor // 100
valor = valor % 100

n50 = valor // 50
valor = valor % 50

n20 = valor // 20
valor = valor % 20

n10 = valor // 10
valor = valor % 10

n5 = valor // 5
valor = valor % 5

n2 = valor // 2
valor = valor % 2

n1 = valor // 1
valor = valor % 1

print(f"{n100} nota(s) de R$100,00")
print(f"{n50} nota(s) de R$50,00")
print(f"{n20} nota(s) de R$20,00")
print(f"{n10} nota(s) de R$10,00")
print(f"{n5} nota(s) de R$5,00")
print(f"{n2} nota(s) de R$2,00")
print(f"{n1} nota(s) de R$1,00")
