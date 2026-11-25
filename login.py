from seguranca import conferir_senha, ler_senha  # compara a senha com o hash e lê a senha com asteriscos

LIMITE_TENTATIVAS = 3  # quantas vezes o usuário pode errar o login


def login_usuario(usuarios):  # recebe o dicionário com todos os usuários cadastrados
    """Retorna o email do usuário logado, ou None se errar demais."""
    for tentativa in range(1, LIMITE_TENTATIVAS + 1):  # repete 3 vezes; "tentativa" vale 1, 2 e 3
        email = input('Digite seu email: ').lower().strip()  # lê o email em minúsculas e sem espaços
        senha = ler_senha('Digite sua senha: ')  # lê a senha mostrando * no lugar de cada caractere

        if email in usuarios and conferir_senha(senha, usuarios[email]["senha"]):  # o email existe E a senha bate com o hash?
            print('Bem-vindo ao CIIU!')  # login certo
            return email  # devolve o email de quem logou

        print(f'Email ou senha incorretos. Tentativa {tentativa} de {LIMITE_TENTATIVAS}')  # mensagem genérica: não revela se o email existe

    print('Limite de tentativas atingido.')  # só chega aqui depois de errar 3 vezes
    return None  # None = "ninguém logado"
