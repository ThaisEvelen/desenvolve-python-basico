#Questão 1
Juliana = int(input("Digite a idade de Juliana:"))
Cris = int(input("Digite a idade de Cris:"))
print(Juliana >17 and Cris > 17)

#Questão 2
Juliana = int(input("Digite a idade de Juliana:"))
Cris = int(input("Digite a idade de Cris:"))
print(Juliana >17 or Cris > 17)

#Questão 3
idade = int(input("Digite sua idade: "))
jogou = input("Já jogou pelo menos 3 jogos de tabuleiro? (Digite True ou False): ")
venceu = int(input("Quantos jogos já venceu? "))
print(16 <= idade <= 18 and jogou == "True" and venceu >= 1)

#Questão 4
personagem = input("Escolha a classe (guerreiro, mago ou arqueiro): ")
força = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))
guerreiro = ((força>=15)and(magia<=10))
mago = ((força<=10)and (magia>=15))
arqueiro =((5 <=força <=15)(5<= magia <=15))
print(guerreiro or mago or arqueiro)