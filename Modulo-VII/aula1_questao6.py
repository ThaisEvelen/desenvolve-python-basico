frase = "o meu amor mora em Roma e me deu um ramo de flores"
objetivo = sorted("amor")

lst_palavras = frase.lower().split(" ")
for palavra in lst_palavras:
    if sorted(palavra)==objetivo:
        print(palavra)
