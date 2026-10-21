def login_usuario(usuarios):

    while True:
        email = input('Digite seu email: ').lower().strip()
        senha = input('Digite sua senha: ')

        if email not in usuarios:
            print('Email não encontrado')
        elif senha != usuarios[email]["senha"]:
            print('senha incorreta')
        else:
            print('Bem-Vindo ao CIIU')
            return email