from dados import carregar  # lê usuários e solicitações do dados.json
from menu import iniciar_menu  # mural e menu principal


def main():  # ponto de entrada do programa
    usuarios, solicitacoes = carregar()  # carrega o que já foi salvo (ou começa vazio)
    iniciar_menu(usuarios, solicitacoes)  # abre o mural e fica no menu até o usuário fechar


if __name__ == "__main__":  # só roda quando você executa "python main.py"
    main()
