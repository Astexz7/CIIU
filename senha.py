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
        print('Senha cadastrada')
        break