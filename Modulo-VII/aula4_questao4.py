import random

with open("gabarito_forca.txt", "w", encoding="utf-8") as f:
    f.write("""computador
girassol
misterio
canguru
borboleta
fantasma
esfinge
violoncelo
astronauta
tornado""")

estagios_lista = [
"""
|---|
|
|
|
=========
""",
"""
|---|
|   o
|
|
=========
""",
"""
|---|
|   o
|   |
|
=========
""",
"""
|---|
|   o
|  /|
|
=========
""",
"""
|---|
|   o
|  /|\\
|
=========
""",
"""
|---|
|   o
|  /|\\
|  /
=========
""",
"""
|---|
|   o
|  /|\\
|  / \\
=========
"""
]
with open("gabarito_enforcado.txt", "w", encoding="utf-8") as f:
    f.write("\n===\n".join(stage.strip() for stage in estagios_lista))

with open("gabarito_forca.txt", "r", encoding="utf-8") as f:
    palavras = f.read().splitlines()

with open("gabarito_enforcado.txt", "r", encoding="utf-8") as f:
    estagios = f.read().strip().split("===")

palavra = random.choice(palavras).lower()
letras_adivinhadas = ["_" for _ in palavra]
letras_erradas = []
tentativas = 0
max_tentativas = 6

def imprime_enforcado(erros):
    print(estagios[erros].strip())

print("Bem-vindo ao jogo da forca!\n")

while tentativas < max_tentativas and "_" in letras_adivinhadas:
    print("\nPalavra:", " ".join(letras_adivinhadas))
    print(f"Erros ({tentativas}/{max_tentativas}): {' '.join(letras_erradas)}")
    letra = input("Digite uma letra: ").lower()

    if not letra.isalpha() or len(letra) != 1:
        print("Digite apenas uma letra válida.")
        continue

    if letra in letras_adivinhadas or letra in letras_erradas:
        print("Você já tentou essa letra.")
        continue

    if letra in palavra:
        for i, l in enumerate(palavra):
            if l == letra:
                letras_adivinhadas[i] = letra
    else:
        letras_erradas.append(letra)
        tentativas += 1
        imprime_enforcado(tentativas - 1)

if "_" not in letras_adivinhadas:
    print("\nParabéns! Você acertou a palavra:", palavra)
else:
    print("\nVocê perdeu! A palavra era:", palavra)
    imprime_enforcado(tentativas)
