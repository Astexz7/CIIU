import os
import secrets
import smtplib
from email.message import EmailMessage
from getpass import getpass
def enviar_codigo(destinatario, codigo):
    remetente = os.environ["EMAIL_REMETENTE"]
    senha_app = os.environ["EMAIL_SENHA_APP"]
    msg = EmailMessage()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = "Código de verificação"
    msg.set_content(f"Seu código de verificação é: {codigo}")
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
        servidor.login(remetente, senha_app)
        servidor.send_message(msg)
usuarios = {}
while True:
    print("1 - Login")
    print("2 - Cadastro")
    print("3 - Sair")
    opcao = input("Escolha uma opção:")
    if opcao == "1":
        print("faça o login")
        usuario = input("digite seu email institucional para login: ")
        senha = getpass("digite sua senha:", echo_char="*")
        if usuario in usuarios and usuarios[usuario] == senha:
            print("Login realizado com sucesso!")
        else:
            print("senha ou usuário inválidos.") 
    elif opcao == "2":
        print ("faça o cadastro")
        email = input("digite seu email institucional: ")
        if email in usuarios:
            print("Este email já cadastrado. Faça o login.")
        elif email.endswith("@ufrpe.br"):
            codigo = f"{secrets.randbelow(10000):04d}"
            enviar_codigo(email, codigo)
            print("código enviado com sucesso!")
            digitado = input("Digite o código: ")
            if digitado == codigo:
                senha = getpass("Crie uma senha: ", echo_char="*")
                usuarios[email] = senha 
                print("cadastro realizado com sucesso!")
            else:
                print("Código inválido.")
        else:
            print("Email inválido. Por favor, utilize um email institucional válido.")   
    elif opcao == "3":
        print("Até logo!")
        break
