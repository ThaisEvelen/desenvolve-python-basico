genero= input("Digite seu genero F ou M :")
idade1 = int(input("Digite sua idade: "))
tempo = int(input("Digite seu tempo de serviço (em anos) :"))
F= idade1>60 or tempo >30 or (idade1 ==60 and tempo >= 25)
M= idade1>65 or tempo >30 or (idade1 ==60 and tempo >= 25)
print((genero =="F" and F) or
      (genero == "M" and M))