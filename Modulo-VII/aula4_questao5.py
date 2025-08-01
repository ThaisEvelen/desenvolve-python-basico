livros = [
    ["1984", "George Orwell", 1949, 328],
    ["O Hobbit", "J.R.R. Tolkien", 1937, 310],
    ["Dom Casmurro", "Machado de Assis", 1899, 256],
    ["A Revolução dos Bichos", "George Orwell", 1945, 112],
    ["Orgulho e Preconceito", "Jane Austen", 1813, 432],
    ["O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96],
    ["Cem Anos de Solidão", "Gabriel García Márquez", 1967, 417],
    ["A Menina que Roubava Livros", "Markus Zusak", 2005, 480],
    ["Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 223],
    ["O Código Da Vinci", "Dan Brown", 2003, 489]
]


with open("meus_livros.csv", "w", encoding="utf-8") as f:
    
    f.write("Título,Autor,Ano de publicação,Número de páginas\n")
    
    for livro in livros:
        linha = f"{livro[0]},{livro[1]},{livro[2]},{livro[3]}\n"
        f.write(linha)

print("Arquivo 'meus_livros.csv' criado com sucesso.")
