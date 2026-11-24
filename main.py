from admin import alterar_status, eh_admin  # funções da parte do administrador
from cadastro import cadastrar  # função que cadastra um novo usuário
from dados import carregar, salvar  # funções que leem e gravam o arquivo dados.json
from login import login_usuario  # função que faz o login
from solicitacoes import fazer_solicitacao, ver_solicitacoes  # funções para criar e listar solicitações


def main():  # função principal: tudo começa aqui
    usuarios, solicitacoes = carregar()  # carrega o que já foi salvo antes (ou começa vazio)
    usuario_logado = None  # None = ninguém logado ainda

    while True:  # o menu se repete até o usuário escolher 0
        print("\n===== CIIU =====")  # título do menu (\n pula uma linha antes)
        if usuario_logado:  # se tem alguém logado...
            tipo = " (administrador)" if eh_admin(usuario_logado) else ""  # texto extra só para admin
            print(f"Logado como: {usuario_logado}{tipo}")  # ...mostra quem é
        print("1 - Cadastrar")
        print("2 - Login")
        print("3 - Nova solicitação")
        print("4 - Ver solicitações")
        print("5 - Sair da conta")
        if eh_admin(usuario_logado):  # opção que só aparece para o administrador
            print("6 - Alterar status de uma solicitação")
        print("0 - Fechar programa")
        opcao = input("Escolha: ").strip()  # lê a opção como texto (por isso comparamos com "1", "2"...)

        if opcao == "1":  # Cadastrar
            cadastrar(usuarios)  # cadastra e coloca o usuário novo no dicionário
            salvar(usuarios, solicitacoes)  # grava no arquivo para não perder
        elif opcao == "2":  # Login
            usuario_logado = login_usuario(usuarios)  # guarda o email de quem logou (ou None se errou)
        elif opcao == "3":  # Nova solicitação
            if usuario_logado:  # só deixa criar se tiver alguém logado
                fazer_solicitacao(solicitacoes, usuario_logado)  # cria a solicitação
                salvar(usuarios, solicitacoes)  # grava no arquivo
            else:  # ninguém logado
                print("Faça login primeiro.")
        elif opcao == "4":  # Ver solicitações
            ver_solicitacoes(solicitacoes, ver_autor_real=eh_admin(usuario_logado))  # admin vê o autor real das anônimas
        elif opcao == "5":  # Sair da conta
            usuario_logado = None  # "esquece" quem estava logado
            print("Você saiu da conta.")
        elif opcao == "6" and eh_admin(usuario_logado):  # só funciona se for admin
            if alterar_status(solicitacoes, usuario_logado):  # True se o status mudou
                salvar(usuarios, solicitacoes)  # grava no arquivo
        elif opcao == "0":  # Fechar programa
            print("Até logo!")
            break  # sai do while, e o programa termina
        else:  # digitou qualquer outra coisa
            print("Opção inválida.")


if __name__ == "__main__":  # só é verdade quando você roda "python main.py" (não quando outro arquivo importa este)
    main()  # chama a função principal
