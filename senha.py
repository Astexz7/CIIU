s= (input('Crie uma senha (Sua senha deve possuir entre 8-20 caracteres, com pelo menos uma letra maiúscula, uma minúscula e um número): '))
sv= input('Digite novamente a senha para confirmação: ')
n=(len(s))
if s == sv:
    if 8 <= n <= 20:
        print('senha cadastrada')
    else:
        print('Senha inválida! Siga as instruções.')
else:
    print('Senhas diferentes.')