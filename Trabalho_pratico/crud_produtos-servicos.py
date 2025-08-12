
import csv
import os
from collections import namedtuple
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

# ----- Configurações -----
ARQUIVO_LIVROS = "livros.txt"
console = Console()

# Estrutura de dados para armazenar livros
Livro = namedtuple("Livro", ["codigo", "titulo", "autor", "preco", "quantidade"])


# ===================== Funções utilitárias =====================

def inicializar_arquivo():
    """
    Cria o arquivo de livros caso não exista, com cabeçalho padrão.
    Entradas: nenhuma
    Saídas: nenhuma
    """
    if not os.path.exists(ARQUIVO_LIVROS):
        with open(ARQUIVO_LIVROS, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["codigo", "titulo", "autor", "preco", "quantidade"])
        console.print(Panel("[green]Arquivo de livros criado[/green]", title="Inicialização"))


def ler_livros():
    """
    Lê todos os livros do arquivo e retorna um dicionário.
    Entradas: nenhuma
    Saídas: dict {codigo: Livro}
    """
    livros = {}
    try:
        with open(ARQUIVO_LIVROS, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)  # pular cabeçalho
            for row in reader:
                if len(row) == 5:
                    codigo, titulo, autor, preco, quantidade = row
                    livros[codigo] = Livro(
                        codigo=codigo,
                        titulo=titulo,
                        autor=autor,
                        preco=float(preco),
                        quantidade=int(quantidade)
                    )
    except FileNotFoundError:
        pass
    return livros


def salvar_livros(livros):
    """
    Salva o dicionário de livros no arquivo.
    Entradas: livros (dict {codigo: Livro})
    Saídas: nenhuma
    """
    with open(ARQUIVO_LIVROS, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["codigo", "titulo", "autor", "preco", "quantidade"])
        for livro in livros.values():
            writer.writerow([livro.codigo, livro.titulo, livro.autor, livro.preco, livro.quantidade])


# ===================== CRUD =====================

def cadastrar_livro(livros):
    """
    Cadastra um novo livro no sistema.
    Entradas: livros (dict {codigo: Livro})
    Saídas: nenhuma
    """
    console.print(Panel("[bold green]Cadastro de Livro[/bold green]", title="Novo Livro"))
    codigo = Prompt.ask("Código do livro")
    if codigo in livros:
        console.print("[red]Código já cadastrado![/red]")
        return
    titulo = Prompt.ask("Título")
    autor = Prompt.ask("Autor")
    preco = float(Prompt.ask("Preço"))
    quantidade = int(Prompt.ask("Quantidade"))

    livros[codigo] = Livro(codigo, titulo, autor, preco, quantidade)
    salvar_livros(livros)
    console.print("[green]Livro cadastrado com sucesso![/green]")


def buscar_livro(livros):
    """
    Busca livros pelo código ou parte do título e exibe os resultados.
    Entradas: livros (dict {codigo: Livro})
    Saídas: nenhuma
    """
    termo = Prompt.ask("Digite o código ou parte do título para buscar").lower()
    encontrados = [
        livro for livro in livros.values()
        if termo in livro.codigo.lower() or termo in livro.titulo.lower()
    ]
    if encontrados:
        for l in encontrados:
            console.print(f"[cyan]{l.codigo}[/cyan] - {l.titulo} ({l.autor}) - R${l.preco:.2f} - Estoque: {l.quantidade}")
    else:
        console.print("[yellow]Nenhum livro encontrado[/yellow]")


def listar_ordenado_nome(livros):
    """
    Lista todos os livros ordenados por título.
    Entradas: livros (dict {codigo: Livro})
    Saídas: nenhuma
    """
    for l in sorted(livros.values(), key=lambda x: x.titulo.lower()):
        console.print(f"[cyan]{l.codigo}[/cyan] - {l.titulo} ({l.autor}) - R${l.preco:.2f} - Estoque: {l.quantidade}")


def listar_ordenado_preco(livros):
    """
    Lista todos os livros ordenados pelo preço (crescente).
    Entradas: livros (dict {codigo: Livro})
    Saídas: nenhuma
    """
    for l in sorted(livros.values(), key=lambda x: x.preco):
        console.print(f"[cyan]{l.codigo}[/cyan] - {l.titulo} ({l.autor}) - R${l.preco:.2f} - Estoque: {l.quantidade}")


def atualizar_livro(livros):
    """
    Atualiza as informações de um livro existente.
    Entradas: livros (dict {codigo: Livro})
    Saídas: nenhuma
    """
    codigo = Prompt.ask("Código do livro a atualizar")
    if codigo not in livros:
        console.print("[red]Livro não encontrado[/red]")
        return
    livro = livros[codigo]
    titulo = Prompt.ask("Novo título", default=livro.titulo)
    autor = Prompt.ask("Novo autor", default=livro.autor)
    preco = float(Prompt.ask("Novo preço", default=str(livro.preco)))
    quantidade = int(Prompt.ask("Nova quantidade", default=str(livro.quantidade)))

    livros[codigo] = Livro(codigo, titulo, autor, preco, quantidade)
    salvar_livros(livros)
    console.print("[green]Livro atualizado com sucesso![/green]")


def excluir_livro(livros):
    """
    Remove um livro do sistema pelo código.
    Entradas: livros (dict {codigo: Livro})
    Saídas: nenhuma
    """
    codigo = Prompt.ask("Código do livro a excluir")
    if codigo in livros:
        del livros[codigo]
        salvar_livros(livros)
        console.print("[green]Livro excluído![/green]")
    else:
        console.print("[yellow]Livro não encontrado[/yellow]")


# ===================== Menu =====================

def menu():
    """
    Exibe o menu principal do sistema de livros e retorna a opção escolhida.
    Entradas: nenhuma
    Saídas: opção (str)
    """
    console.print(Panel("📚 [bold green]Sistema de Livros[/bold green]", title="Menu"))
    console.print("1. Cadastrar Livro")
    console.print("2. Buscar Livro")
    console.print("3. Listar por Nome")
    console.print("4. Listar por Preço")
    console.print("5. Atualizar Livro")
    console.print("6. Excluir Livro")
    console.print("0. Sair")

    while True:
        opcao = Prompt.ask("Escolha uma opção")
        if opcao in ["0", "1", "2", "3", "4", "5", "6"]:
            return opcao
        else:
            console.print("[red]Opção inválida! Digite um número de 0 a 6.[/red]")

# ===================== Principal =====================

def main():
    """
    Função principal que executa o loop do sistema.
    Entradas: nenhuma
    Saídas: nenhuma
    """
    inicializar_arquivo()
    livros = ler_livros()

    while True:
        opcao = menu()
        if opcao == "1":
            cadastrar_livro(livros)
        elif opcao == "2":
            buscar_livro(livros)
        elif opcao == "3":
            listar_ordenado_nome(livros)
        elif opcao == "4":
            listar_ordenado_preco(livros)
        elif opcao == "5":
            atualizar_livro(livros)
        elif opcao == "6":
            excluir_livro(livros)
        elif opcao == "0":
            console.print("[bold magenta]Saindo...[/bold magenta]")
            break


if __name__ == "__main__":
    main()
