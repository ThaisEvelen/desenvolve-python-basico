num = input("Digite o número: ")


if len(num) == 8:
    num = '9' + num

if len(num) == 9 and num[0] == '9':
    numero_formatado = num[:5] + '-' + num[5:]
    print("Número completo:", numero_formatado)
else:
    print("Número inválido")

