ano= int(input("Digite o ano que deseja consultar: "))
if ano % 4 ==0 and ano % 100 != 0 or ano % 400 ==0:
    print("Bissexto")
else:
    print("Não bissexto")