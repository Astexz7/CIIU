#CADASTRO DE EMAIL

import random

print('Bem-Vindo ao CIIU.')
print('Vamos fazer seu cadastro')

#função criada para verificar final do email institucional
def email_inst(email):

    #aqui verifica o final do email
    if email.endswith("@ufrpe.br"):
        return True
    else:
        return False

#aqui faz o loop em caso de erro
while True:

    #aqui digita-se o email do usuário
    email = input('Digite seu email institucional (@ufrpe.br): ').lower()

    #verificação de verdadeiro ou falso
    if  email_inst(email):
        print(f"Enviamos um código para o seu email: {email}")
        break

    else:
        print("Aceitamos apenas email's institucionais")

#VERIFICAÇÃO DE EMAIL

cod = random.randint(1000,9999)
print(cod)

erros = 0
lim_erros = 3

while True:

    cod_verif = int(input('Digite o código enviado para seu email verifica-lo: '))

    if cod == cod_verif:
        print('Email verificado')
        break

    else:
        erros += 1

        if lim_erros > erros:
            print(f'Código incorreto. Tentativa {erros} de {lim_erros}')
        
        else:
            print('Limite de tentativas atingido.')
            break

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

        if caracteres.isupper():
            tem_maiscula = True
        if caracteres.islower():
            tem_minuscula= True
        if caracteres.isdigit():
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

#ESCOLHA DE CURSO

#lista de cursos
list_courses = ['BSI', 'BMV', 'BCC', 'LCC' ]
print({list_courses})

while True:
    escolha = input('Digite seu curso: ').strip().upper()

    if escolha in list_courses:
        print(f'Curso {escolha} escolhido com sucesso')
        break
    else:
        print('Curso inválido')