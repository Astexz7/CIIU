import hashlib  # biblioteca do Python que cria "hashes" (códigos embaralhados que não dá para desfazer)
import hmac  # biblioteca usada aqui para comparar os hashes de forma segura
import os  # biblioteca do sistema; usamos para gerar bytes aleatórios
import sys  # usado para ler o teclado tecla por tecla e escrever os asteriscos
from getpass import getpass  # plano B: lê a senha escondida quando não há um terminal de verdade


def gerar_hash(senha):  # recebe a senha digitada e devolve o texto que vai ser guardado
    """Transforma a senha em um hash seguro para guardar."""
    sal = os.urandom(16)  # gera 16 bytes aleatórios (o "sal"); assim duas senhas iguais viram hashes diferentes
    h = hashlib.pbkdf2_hmac("sha256", senha.encode(), sal, 200_000)  # embaralha a senha junto com o sal 200 mil vezes (fica lento para quem tenta adivinhar)
    return sal.hex() + ":" + h.hex()  # converte sal e hash para texto e junta os dois com ":" no meio


def conferir_senha(senha, guardado):  # recebe a senha digitada no login e o texto guardado no cadastro
    """Confere se a senha digitada bate com o hash guardado."""
    sal_hex, h_hex = guardado.split(":")  # separa o texto guardado em duas partes: o sal e o hash
    h = hashlib.pbkdf2_hmac("sha256", senha.encode(), bytes.fromhex(sal_hex), 200_000)  # refaz o hash da senha digitada usando o MESMO sal do cadastro
    return hmac.compare_digest(h.hex(), h_hex)  # compara os dois hashes; True se forem iguais (senha certa), False se não


def _ler_tecla():  # lê UMA tecla, sem esperar o Enter (o "_" no nome indica uso interno)
    """Devolve a tecla apertada, ou "" para teclas especiais (setas, F1...)."""
    try:
        import msvcrt  # só existe no Windows
    except ImportError:  # não é Windows: usamos termios/tty (Linux e macOS)
        import termios
        import tty
        fd = sys.stdin.fileno()  # número que identifica o teclado para o sistema
        config_antiga = termios.tcgetattr(fd)  # guarda a configuração atual do terminal
        try:
            tty.setraw(fd)  # modo "cru": o terminal entrega cada tecla na hora e não mostra nada
            tecla = sys.stdin.read(1)
            if tecla == "\x1b":  # setas e outras teclas especiais começam com ESC...
                sys.stdin.read(2)  # ...e mandam mais 2 caracteres, que descartamos
                return ""
            return tecla
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, config_antiga)  # devolve o terminal ao normal
    tecla = msvcrt.getwch()  # Windows: lê uma tecla sem mostrar na tela
    if tecla in ("\x00", "\xe0"):  # teclas especiais no Windows vêm em duas partes...
        msvcrt.getwch()  # ...descartamos a segunda
        return ""
    return tecla


def ler_senha(pergunta):  # igual ao input, mas mostra * no lugar de cada caractere
    """Lê a senha mostrando um asterisco para cada caractere digitado."""
    if not sys.stdin.isatty():  # sem terminal de verdade (ex.: console de algumas IDEs)...
        return getpass(pergunta)  # ...usa o getpass, que esconde a senha sem asteriscos

    print(pergunta, end="", flush=True)  # mostra a pergunta sem pular linha
    senha = ""  # aqui vamos juntando os caracteres digitados
    while True:  # repete a cada tecla, até o Enter
        tecla = _ler_tecla()
        if tecla in ("\r", "\n"):  # Enter: terminou de digitar
            print()  # pula a linha
            return senha
        if tecla == "\x03":  # Ctrl+C: encerra o programa, como de costume
            raise KeyboardInterrupt
        if tecla in ("\x08", "\x7f"):  # Backspace (Windows usa \x08; Linux/macOS usam \x7f)
            if senha:  # só apaga se tiver algo digitado
                senha = senha[:-1]  # tira o último caractere da senha
                print("\b \b", end="", flush=True)  # volta o cursor, escreve um espaço por cima do * e volta de novo
        elif tecla and tecla.isprintable():  # letra, número ou símbolo ("" = tecla especial, ignorada)
            senha += tecla  # guarda o caractere de verdade
            print("*", end="", flush=True)  # mas mostra só um asterisco
