distancia= int(input("Digite a distância en km: "))
Peso = int(input("Digite o peso do pacote em kg:"))
if distancia == 100:
    valor = 1 * Peso
if 100< distancia <300:
    valor = 1.50 * Peso
if distancia> 300:
    valor = 2 * Peso
if Peso >= 10:
    valor = valor + 10

print("O valor do frete é: ",valor,"reais")
