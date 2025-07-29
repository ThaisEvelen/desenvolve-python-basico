import random

def encrypt(lista_nomes):
    chave = random.randint(1, 10)
    nomes_criptografados = []

    for nome in lista_nomes:
        criptografado = ''
        for letra in nome:
            novo_codigo = ord(letra) + chave
            if novo_codigo > 126:
                novo_codigo = 33 + (novo_codigo - 127)
            criptografado += chr(novo_codigo)
        nomes_criptografados.append(criptografado)

    return nomes_criptografados, chave

entrada = input("Digite os nomes separados por vírgula: ")  
lista_nomes = [nome.strip() for nome in entrada.split(",")]

criptografados, chave = encrypt(lista_nomes)

print("Chave aleatória:", chave)
print("Nomes criptografados:", criptografados)
