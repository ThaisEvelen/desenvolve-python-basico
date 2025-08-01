import re

f = open("C:\\Users\\PDITA840\\Documents\\GitHub\\desenvolve-python-basico\\Modulo-VII\\estomago.txt", "r", encoding="utf-8")
linhas=f.readlines()
print('Número de linhas',len(linhas))
print('Primeiras 25 linhas:')
for linha in linhas[:25]:
    print(linha.strip())

maior_linha = max(linhas, key=len)
print('\nLinha com mais caracteres:')
print(maior_linha.strip())
print('Número de caracteres:', len(maior_linha))

texto = " ".join(linhas).lower()
nonato = re.findall(r'\bnonato\b', texto)
iria = re.findall(r'\bíria\b', texto)

print('\nNúmero de menções a "Nonato":', len(nonato))
print('Número de menções a "Íria":', len(iria))

f.close()