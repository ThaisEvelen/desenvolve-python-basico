# main.py

import csv
import os
from collections import namedtuple
from getpass import getpass

from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text

# ----- Constantes e variáveis globais -----
ARQUIVO_USUARIOS = 'usuarios.txt'
USUARIO_LOGADO = None  # será um namedtuple Usuario quando alguém logar

# ----- Console (rich) -----
console = Console()

# ===================== Funções utilitárias =====================

def inicializar_arquivo(arquivo_csv):
    """
    Garante que o arquivo exista e tenha pelo menos um admin.
    Se o arquivo não existir, cria com o usuário padrão:
      login: admin
      senha: admin
      tipo: admin
    Se existir mas estiver vazio, também cria o admin padrão.
    """
    precisa_criar = False
    if not os.path.exists(arquivo_csv):
        precisa_criar = True
    else:
        # se arquivo existir mas estiver vazio -> criar entrada admin
        if os.path.getsize(arquivo_csv) == 0:
            precisa_criar = True

    if precisa_criar:
        with open(arquivo_csv, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['admin', 'admin', 'admin'])
        console.print(Panel("[bold green]Arquivo de usuários criado com admin padrão[/bold green]\nUsuário: [bold]admin[/bold]  Senha: [bold]admin[/bold]",
                            title="Inicialização", expand=False))


def ler_usuarios(arquivo_csv):
    """
    Lê o arquivo CSV e retorna um dicionário:
      chave -> login
      valor -> namedtuple Usuario(login, senha, tipo)

    Observações:
      - Ignora linhas que não tenham exatamente 3 campos.
      - Faz strip() nos campos para evitar espaços extras.
    """
    Usuario = namedtuple('Usuario', ['login', 'senha', 'tipo'])
    usuarios = {}

    # Se o arquivo não existir, retorna dicionário vazio (chame inicializar_arquivo antes)
    if not os.path.exists(arquivo_csv):
        return usuarios

    try:
        with open(arquivo_csv, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                # ignora linhas vazias ou malformadas
                if not row:
                    continue
                if len(row) != 3:
                    # linha inválida: não contém login, senha e tipo
                    continue
                nome_usuario, senha, tipo = [col.strip() for col in row]
                usuarios[nome_usuario] = Usuario(login=nome_usuario, senha=senha, tipo=tipo)
    except Exception as e:
        console.print(f"[bold red]Erro ao ler arquivo de usuários:[/bold red] {e}")

    return usuarios

# ===================== Funções CRUD (mantendo nomes originais) =====================

##### CRUD Read
# Função para realizar login de um usuário.
# Atualiza a variável global USUARIO_LOGADO em caso de login bem sucedido.
# Parâmetro: usuarios (dict) - dicionário de usuários retornado por ler_usuarios().
# Retorno: None (altera a variável global USUARIO_LOGADO)
def fazer_login(usuarios):
    global USUARIO_LOGADO

    console.print(Panel("🟢 [bold green]Login[/bold green] 🟢\n\nPor favor, insira suas credenciais.", 
                        expand=False, title="Tela de Login"))
    username = Prompt.ask("[bold cyan]Nome de Usuário[/bold cyan]")
    senha = getpass("Senha: ")

    user = usuarios.get(username, None)
    if user is not None and user.senha == senha:
        console.print("\n[bold green]Login bem-sucedido![/bold green]")
        USUARIO_LOGADO = user
    else:
        console.print(f"[bold red]Erro: usuário ou senha incorretos![/bold red]")


##### CRUD Create
# Função para cadastrar um novo usuário.
# Parâmetros:
#   usuarios (dict) - dicionário atual de usuários
#   arquivo_csv (str) - caminho do arquivo onde será salvo
# Retorno: nome do novo usuário (str) em caso de sucesso, ou False em caso de falha
def cadastrar_usuario(usuarios, arquivo_csv):
    console.print(Panel("[bold green]Cadastro de Novo Usuário[/bold green]\nPor favor, insira os dados do novo usuário.", 
                        title="Novo Usuário", expand=False))

    nome_usuario = Prompt.ask("[bold cyan]Nome de Usuário[/bold cyan]").strip()
    senha = getpass("Senha: ")

    # controle de acesso: somente admin pode escolher o tipo (admin/cliente)
    if USUARIO_LOGADO is not None and USUARIO_LOGADO.tipo == 'admin':
        tipo = Prompt.ask("[bold cyan]Tipo de Usuário (admin/cliente)[/bold cyan]", choices=["admin", "cliente"])
    else:
        tipo = 'cliente'

    # verifica existência
    if usuarios.get(nome_usuario, None) is not None:
        console.print(f"[bold red]Erro:[/bold red] Usuário '[bold red]{nome_usuario}[/bold red]' já existe!")
        return False
    else:
        try:
            with open(arquivo_csv, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([nome_usuario, senha, tipo])
            console.print(f"[bold green]Usuário '{nome_usuario}' cadastrado com sucesso![/bold green]")
            return nome_usuario
        except Exception as e:
            console.print(f"[bold red]Erro ao gravar usuário:[/bold red] {e}")
            return False


##### CRUD Delete
# Remove um usuário do arquivo.
# Parâmetros:
#   usuarios (dict) - dicionário atual de usuários
#   arquivo_csv (str) - caminho do arquivo onde está salvo
# Retorno: True se excluído, False caso contrário
def excluir_usuario(usuarios, arquivo_csv):
    console.print(Panel("[bold red]Exclusão de Usuário[/bold red]\nPor favor, insira o nome do usuário a ser excluído.", 
                        title="Excluir Usuário", expand=False))
    nome_usuario = Prompt.ask("[bold cyan]Nome de Usuário[/bold cyan]").strip()

    if usuarios.get(nome_usuario, None) is not None:
        try:
            # reescreve todo o arquivo sem o usuário excluído
            with open(arquivo_csv, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                for usuario in usuarios.values():
                    if usuario.login != nome_usuario:
                        writer.writerow([usuario.login, usuario.senha, usuario.tipo])
            console.print(f"[bold green]Usuário '{nome_usuario}' excluído com sucesso![/bold green]")
            return True
        except Exception as e:
            console.print(f"[bold red]Erro ao excluir usuário:[/bold red] {e}")
            return False
    else:
        console.print(f"[bold yellow]Usuário '{nome_usuario}' não encontrado![/bold yellow]")
        return False
    

##### CRUD Update
# Atualiza a senha de um usuário.
# Admins podem atualizar qualquer usuário; clientes apenas sua própria senha.
def atualiza_senha(usuarios, arquivo_csv):
    global USUARIO_LOGADO

    if USUARIO_LOGADO is None:
        console.print("[bold red]Essa função não deve ser chamada sem um usuário logado!!![/bold red]")
        return False

    if USUARIO_LOGADO.tipo == 'cliente':
        console.print(Panel("[bold yellow]Atualização de Senha[/bold yellow]\nPor favor, informe a nova senha desejada.", 
                            title="Atualizar Senha", expand=False))
        nome_usuario = USUARIO_LOGADO.login
    else:
        console.print(Panel("[bold yellow]Atualização de Senha[/bold yellow]\nPor favor, insira o nome do usuário cuja senha será atualizada.", 
                            title="Atualizar Senha", expand=False))
        nome_usuario = Prompt.ask("[bold cyan]Nome de Usuário[/bold cyan]").strip()
    
    nova_senha = getpass("Nova senha: ")

    if usuarios.get(nome_usuario, None) is not None:
        try:
            with open(arquivo_csv, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                for _, usuario in usuarios.items():
                    if usuario.login != nome_usuario:
                        writer.writerow([usuario.login, usuario.senha, usuario.tipo])
                    else:
                        writer.writerow([usuario.login, nova_senha, usuario.tipo])
            console.print(f"[bold green]Senha do usuário '{nome_usuario}' atualizada com sucesso![/bold green]")
            return True
        except Exception as e:
            console.print(f"[bold red]Erro ao atualizar senha:[/bold red] {e}")
            return False
    else:
        console.print(f"[bold yellow]Usuário '{nome_usuario}' não encontrado![/bold yellow]")
        return False

# ===================== Menus (visual) =====================

def menu_inicial():
    """
    Exibe o menu inicial com estilo parecido com a captura de tela:
     - painel com título
     - opções numeradas e coloridas
    """
    console.print()
    console.print(Panel("[bold green]Sistema de brincadeirinha![/bold green]\nEscolha uma das opções abaixo:", title="Menu Inicial", expand=False))
    console.print("[bold cyan]1.[/bold cyan] [bold white]Fazer Login[/bold white]")
    console.print("[bold cyan]2.[/bold cyan] [bold white]Cadastro[/bold white]")
    console.print("[bold cyan]3.[/bold cyan] [bold white]Sair do sistema[/bold white]")
    console.print()
    opcao = Prompt.ask("[bold yellow]Digite o número da opção desejada[/bold yellow]", choices=["1", "2", "3"])
    return opcao

def menu_interno():
    """
    Menu apresentado após login. Administradores têm opções extras.
    """
    console.print()
    console.print(Panel(f"[bold green]Olá {USUARIO_LOGADO.login}![/bold green]\nEscolha uma das opções abaixo:", title="Menu Interno", expand=False))
    
    if USUARIO_LOGADO.tipo == 'admin':
        console.print("[bold cyan]1.[/bold cyan] [bold white]Atualizar cadastro[/bold white]")
        console.print("[bold cyan]2.[/bold cyan] [bold white]Excluir cadastro[/bold white]")
        console.print("[bold white]Para fazer logout digite[/bold white] [bold cyan]0[/bold cyan]")
        opcao = Prompt.ask("[bold yellow]Digite o número da opção desejada[/bold yellow]", choices=["0","1", "2"])
    else:
        console.print("[bold cyan]1.[/bold cyan] [bold white]Atualizar cadastro[/bold white]")
        console.print("[bold white]Para fazer logout digite[/bold white] [bold cyan]0[/bold cyan]")
        opcao = Prompt.ask("[bold yellow]Digite o número da opção desejada[/bold yellow]", choices=["0","1"])
    return  opcao

# ===================== Fluxo principal =====================

def main():
    global USUARIO_LOGADO

    # garante que o arquivo exista antes de tentar ler
    inicializar_arquivo(ARQUIVO_USUARIOS)
    usuarios = ler_usuarios(ARQUIVO_USUARIOS)

    while True:
        opcao = menu_inicial()
        if opcao == "1":
            # usa a função separada de login (como no seu original)
            fazer_login(usuarios)
        elif opcao == "2":
            novo_user = cadastrar_usuario(usuarios, ARQUIVO_USUARIOS)
            if novo_user != False:
                # recarrega dicionário e loga automaticamente o novo usuário
                usuarios = ler_usuarios(ARQUIVO_USUARIOS)
                USUARIO_LOGADO = usuarios.get(novo_user)
        elif opcao == "3":
            console.print(Panel("[bold magenta]Até mais![/bold magenta]\nSaindo do sistema...", expand=False))
            break
        else:
            console.print(f"[bold yellow]Opção inválida![/bold yellow]")

        # se alguém logou, entra no menu interno
        if USUARIO_LOGADO is not None:
            while True:
                opcao = menu_interno()
                if opcao == '0':
                    # logout
                    USUARIO_LOGADO = None
                    console.print("[bold cyan]Logout realizado.[/bold cyan]")
                    break
                elif opcao == "1":
                    # atualizar senha (clientes atualizam a própria, admin pode atualizar qualquer)
                    if atualiza_senha(usuarios, ARQUIVO_USUARIOS):
                        usuarios = ler_usuarios(ARQUIVO_USUARIOS)
                        # atualiza referência do usuário logado caso a senha dele tenha mudado
                        USUARIO_LOGADO = usuarios.get(USUARIO_LOGADO.login)
                elif opcao == "2":
                    # excluir: apenas admins vêem essa opção no menu_interno
                    if excluir_usuario(usuarios, ARQUIVO_USUARIOS):
                        usuarios = ler_usuarios(ARQUIVO_USUARIOS)
                        # Se o usuário excluído for o que está logado, desloga
                        if USUARIO_LOGADO and USUARIO_LOGADO.login not in usuarios:
                            console.print("[bold cyan]Você excluiu seu próprio usuário. Fazendo logout...[/bold cyan]")
                            USUARIO_LOGADO = None
                            break
                else:
                    console.print(f"[bold yellow]Opção inválida![/bold yellow]")

if __name__ == "__main__":
    main()
