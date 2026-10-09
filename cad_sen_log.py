print('Bem-Vindo ao CIIU.')

def email_restriçoes(email):

    termino = False

    caracteres in email
    if .endswith('@ufrpe.br'):
            termino = True

while True:

    email = input('Digite seu email institucional (@ufrpe.br): ').lower

    print(email)
    print(email_restriçoes)

    if email != email_restriçoes:
        print('Seu email precisa terminar em: @Ufrpe.br')
    else:
        print(f'Enviamos um código para verificação no email {email}')
        break

print(email)
print(email_restriçoes)