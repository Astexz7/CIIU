import secrets  # biblioteca para gerar números aleatórios seguros (melhor que "random" para códigos)
import smtplib  # biblioteca para enviar emails
from email.message import EmailMessage  # classe que monta o email (remetente, destinatário, assunto, texto)
from getpass import getpass  # função igual ao input, mas que esconde o que é digitado (para senhas)

from cursos import selecionar_curso_usuario  # importa a função que mostra a lista de cursos
from seguranca import gerar_hash  # importa a função que transforma a senha em hash

SENHA_AAAPP = 'jnzs ooga iiof wmbu'  # senha de app do Gmail do projeto
EMAIL_PROJETO = "projetociiu@gmail.com"  # email que envia os códigos de verificação
LIMITE_ERROS = 3  # quantas vezes o usuário pode errar o código


def email_inst(email):  # verifica se o email é institucional
    """Aceita apenas emails no formato algo@ufrpe.br."""
    usuario, _, dominio = email.partition("@")  # divide o email no "@": o que vem antes (usuario) e depois (dominio)
    return dominio == "ufrpe.br" and len(usuario) > 0  # válido só se o domínio for ufrpe.br e tiver algo antes do @


def senha_valida(senha):  # verifica se a senha segue as regras
    """8 a 20 caracteres, com maiúscula, minúscula e número."""
    return (8 <= len(senha) <= 20  # o tamanho precisa estar entre 8 e 20 caracteres
            and any(c.isupper() for c in senha)  # any = "pelo menos um"; aqui: pelo menos uma letra maiúscula
            and any(c.islower() for c in senha)  # pelo menos uma letra minúscula
            and any(c.isdigit() for c in senha))  # pelo menos um número


def enviar_codigo(email, cod):  # manda o código de verificação para o email do aluno
    """Envia o código por email. Retorna True se deu certo."""
    msg = EmailMessage()  # cria um email vazio
    msg["From"] = EMAIL_PROJETO  # quem envia
    msg["To"] = email  # quem recebe
    msg["Subject"] = 'Centro de Informação Infraestrutural Universitário (CIIU)'  # assunto do email
    msg.set_content(f"Seu código de verificação é {cod}")  # texto do email, com o código dentro

    try:  # "tente" fazer o envio; se der erro, pula para o except em vez de fechar o programa
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:  # conecta no servidor do Gmail (porta 465, com criptografia)
            servidor.login(EMAIL_PROJETO, SENHA_AAAPP)  # faz login na conta do projeto
            servidor.send_message(msg)  # envia o email
        return True  # se chegou aqui, deu certo
    except (smtplib.SMTPException, OSError) as erro:  # pega erros de email ou de internet
        print(f"Não foi possível enviar o email: {erro}")  # mostra o erro para o usuário
        return False  # avisa quem chamou que não deu certo


def verificar_codigo(cod):  # pede o código ao usuário e confere
    """Dá ao usuário até LIMITE_ERROS tentativas. Retorna True se acertou."""
    for tentativa in range(1, LIMITE_ERROS + 1):  # repete 3 vezes; "tentativa" vale 1, depois 2, depois 3
        cod_verif = input('Digite o código enviado para seu email: ').strip()  # lê o código; strip tira espaços sobrando
        if cod_verif == cod:  # se o código digitado for igual ao enviado...
            print('EMAIL VERIFICADO!')  # ...avisa que deu certo
            return True  # e sai da função com sucesso
        print(f'Código incorreto. Tentativa {tentativa} de {LIMITE_ERROS}')  # se errou, mostra quantas tentativas já foram
    print('Limite de tentativas atingido.')  # só chega aqui se errou as 3 vezes
    return False  # sai da função indicando falha


def pedir_email(usuarios):  # pede o email até conseguir um válido e verificado
    """Pede o email até ele ser válido, novo e verificado."""
    while True:  # repete até dar "return" lá embaixo
        email = input('Digite seu email institucional (@ufrpe.br): ').lower().strip()  # lê o email em minúsculas e sem espaços

        if not email_inst(email):  # se NÃO for email institucional...
            print("Aceitamos apenas emails institucionais (@ufrpe.br).")  # ...avisa
            continue  # e volta para o início do while (pede de novo)

        if email in usuarios:  # se o email já está no dicionário de usuários...
            print("Este email já está cadastrado.")  # ...avisa
            continue  # e pede outro

        cod = f"{secrets.randbelow(10000):04d}"  # sorteia um número de 0 a 9999 e completa com zeros (ex: 0042)
        if not enviar_codigo(email, cod):  # tenta enviar; se falhar...
            continue  # ...pede o email de novo

        print(f"Enviamos um código para o seu email: {email}")  # confirma o envio
        if verificar_codigo(cod):  # se o usuário acertar o código...
            return email  # ...devolve o email e sai da função


def pedir_senha():  # pede a senha até ela ser válida e confirmada
    """Pede a senha até ela seguir as regras e ser confirmada."""
    while True:  # repete até dar "return"
        senha = getpass('Crie uma senha (8-20 caracteres, com pelo menos uma letra '  # lê a senha sem mostrar na tela
                        'maiúscula, uma minúscula e um número): ')  # (continuação do texto da linha de cima)
        senha_verificacao = getpass('Digite novamente a senha para confirmação: ')  # pede a senha de novo

        if senha != senha_verificacao:  # se as duas forem diferentes...
            print('Senhas diferentes.')  # ...avisa e o while repete
        elif not senha_valida(senha):  # se forem iguais, mas não seguirem as regras...
            print('Senha fora do padrão.')  # ...avisa e o while repete
        else:  # se estiver tudo certo...
            print('Senha criada.')  # ...confirma
            return senha  # e devolve a senha


def cadastrar(usuarios):  # função principal do cadastro; recebe o dicionário de usuários
    email = pedir_email(usuarios)  # 1º passo: email válido e verificado
    senha = pedir_senha()  # 2º passo: senha válida
    curso = selecionar_curso_usuario()  # 3º passo: escolha do curso
    usuarios[email] = {'senha': gerar_hash(senha), 'curso': curso}  # salva o usuário (o email é a chave; a senha vai como hash)
    print('Cadastro concluído!')  # avisa que terminou
