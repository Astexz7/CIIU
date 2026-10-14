import random
from email.message import EmailMessage
import smtplib


print('Bem-Vindo ao CIIU.')
SENHA_AAAPP = 'jnzs ooga iiof wmbu'

def email_inst(email):

    if email.endswith("@ufrpe.br"): #verificação se o email termina com @ufrpe.br
        return True
    else:
        return False

while True: #aqui faz o loop em caso de erro

    email = input('Digite seu email institucional (@ufrpe.br): ').lower() #aqui digita-se o email do usuário


    if  email_inst(email): #VERIFICAÇÃO DE EMAIL

        cod = str(random.randint(1000,9999)) #geração de código aleatório

        #dados dos email´s
        msg = EmailMessage()
        msg["From"] = "projetociiu@gmail.com"
        msg["To"] = email
        msg["Subject"] = 'Centro de Informação Infraestrutural Universitário (CIIU)'
        msg.set_content(f"Seu código de verificação é {cod}")

        #porta do servido e senha do email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
            servidor.login("projetociiu@gmail.com", SENHA_AAAPP)
            servidor.send_message(msg)

        print(f"Enviamos um código para o seu email: {email}")

        erros = 0 #variável de quantidade inicial de erros
        lim_erros = 3 #limite de erros
        verif_email = False #variável para constar se o email foi verificado

        while True:
            cod_verif = (input('Digite o código enviado para seu email verifica-lo: ')) #usuário digita o código aqui

            if cod != cod_verif: #aqui soma mais 1 erro a cada tentativa falha
                erros += 1

                if lim_erros > erros: #aqui verifica se a quantidade de erro ultrapassou o limite permitido
                    print(f'Código incorreto. Tentativa {erros} de {lim_erros}')
                
                else:
                    print('Limite de tentativas atingido.')
                    break
            else:
                print('EMAIL VERIFICADO!')
                verif_email = True
                break

        if verif_email:
            break
    else:
        print("Aceitamos apenas email's institucionais")

#CRIAÇÃO DE SENHA

def senha_valida(senha):

    #conta quantos caracteres a variável "senha" possue
    qnt_caracteres = (len(senha))

    #três variáveis, que caso nada seja digitado ou não acate as restrições, elas considerem como falsas.    
    tem_maiscula = False
    tem_minuscula = False
    tem_numero = False

    #verificação de caracteres na senha p1.
    for caracteres in senha:

        if caracteres.isupper(): #verifica se a senha possui letra maiúscula
            tem_maiscula = True
        if caracteres.islower(): #verifica se a senha possui letra minúscula
            tem_minuscula= True
        if caracteres.isdigit(): #verifica se a senha possui número
            tem_numero = True

    #verificação de caracteres na senha p2.
    if tem_maiscula and tem_minuscula and tem_numero:

        #verificação de respeito a quatidade de caracteres mínimos e máximos.   
        if 8 <= qnt_caracteres <= 20:
                return True
        
        else:
            return False
    else:
        return False
    
#loop para em caso de não obidência as regras.
while True:

    #caixa de dígito para criação de senha.    
    senha = (input('Crie uma senha (Sua senha deve possuir de 8-20 caracteres, com pelo menos uma letra maiúscula, uma minúscula e um número): '))

    #caixa de senha de verificação.
    senha_verificacao = input('Digite novamente a senha para confirmação: ')

    #verificação se a senha é diferente da senha de verificação.
    if senha != senha_verificacao:
        print('Senhas diferentes.')

    #verificação se a senha acata as regras permitidas.
    elif not senha_valida(senha):
        print('Senha fora do padrão')

    #afirmação de acatamento as restrições impostas.
    else:
        print('Senha criada')
        break

usuario[email] = {'senha' : senha}
