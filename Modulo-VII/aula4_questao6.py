import csv


mais_tocadas_por_ano = {}


with open("C:\\Users\\PDITA840\\Documents\\GitHub\\desenvolve-python-basico\\Modulo-VII\\spotify-2023.csv", "r", encoding="latin-1") as f:
    leitor = csv.DictReader(f)

    for linha in leitor:
        try:
            nome_musica = linha["track_name"]
            artista = linha["artist(s)_name"]
            ano = int(linha["released_year"])
            streams = int(linha["streams"])
            artista_count = int(linha["artist_count"])

            if '"' in nome_musica or '"' in artista:
                continue

            if ano < 2012 or ano > 2022:
                continue

            if ano not in mais_tocadas_por_ano or streams > mais_tocadas_por_ano[ano][3]:
                mais_tocadas_por_ano[ano] = [nome_musica, artista, ano, streams]

        except (ValueError, KeyError):
            continue  

lista_final = [mais_tocadas_por_ano[ano] for ano in sorted(mais_tocadas_por_ano)]

print(lista_final)
