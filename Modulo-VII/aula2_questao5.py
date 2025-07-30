import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    nova_frase = []

    for palavra in palavras:
        if len(palavra) <= 3:
            nova_frase.append(palavra)
        else:
            primeira = palavra[0]
            ultima = palavra[-1]
            meio = list(palavra[1:-1])
            random.shuffle(meio)
            palavra_embaralhada = primeira + ''.join(meio) + ultima
            nova_frase.append(palavra_embaralhada)

    return ' '.join(nova_frase)

entrada = input("Digite uma frase para embaralhar: ")
resultado = embaralhar_palavras(entrada)
print("Frase embaralhada:", resultado)