frase = "O meu amor mora em Roma e me deu um ramo de flores"

count_vogais = 0
indices=[]
for i  in range(len(frase)):
    if frase[i] in "aeiouAEIOU":
        count_vogais +=1
        indices.append(i)
print(count_vogais)
print(indices)