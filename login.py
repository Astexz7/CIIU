from seguranca import ler_senha  # lê a senha mostrando * no lugar de cada caractere

LIMITE_TENTATIVAS = 3  # quantas vezes o usuário pode errar o login


def login_usuario(usuarios):  # recebe o dicionário com todos os usuários cadastrados
    """Retorna o objeto do usuário logado, ou None se errar demais."""
    for tentativa in range(1, LIMITE_TENTATIVAS + 1):  # repete 3 vezes; "tentativa" vale 1, 2 e 3
        email = input('Digite seu email: ').lower().strip()  # lê o email em minúsculas e sem espaços
        senha = ler_senha('Digite sua senha: ')  # lê a senha mostrando * no lugar de cada caractere

        usuario = usuarios.get(email)  # o objeto do usuário, ou None se o email não existir
        if usuario and usuario.senha_correta(senha):  # o email existe E a senha bate com o hash?
            print(f'Bem-vindo ao CIIU! Você entrou como {usuario.tipo}.')  # login certo
            return usuario  # devolve o objeto de quem logou

        print(f'Email ou senha incorretos. Tentativa {tentativa} de {LIMITE_TENTATIVAS}')  # mensagem genérica: não revela se o email existe

    print('Limite de tentativas atingido.')  # só chega aqui depois de errar 3 vezes
    return None  # None = "ninguém logado"
