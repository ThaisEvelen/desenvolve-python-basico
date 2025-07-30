def validador_senha(senha):
    if len(senha) < 8:
        return False

    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False

    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_numero = True
        elif caractere in "@#$":
            tem_especial = True

    return tem_maiuscula and tem_minuscula and tem_numero and tem_especial

senha_usuario = input("Digite sua senha: ")

if validador_senha(senha_usuario):
    print("Senha válida ")
else:
    print("Senha inválida ")
