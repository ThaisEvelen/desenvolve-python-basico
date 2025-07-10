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
