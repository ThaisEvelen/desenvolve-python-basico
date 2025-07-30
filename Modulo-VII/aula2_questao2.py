frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"

for vogal in vogais:
    frase = frase.replace(vogal, "*")

print("Frase modificada:", frase)
