import os  # usado para saber se o sistema é Windows (os.name == 'nt')
import subprocess  # usado para rodar o comando que limpa a tela

from cadastro import cadastrar  # cadastro de usuário
from comunidade import comentar, ver_ranking, votar_prioridade  # enquete, comentários e ranking
from dados import salvar  # grava os dados no dados.json
from login import login_usuario  # login
from solicitacoes import Solicitacao, fazer_solicitacao, ver_detalhes, ver_solicitacoes  # classe e funções das solicitações
from usuarios import Usuario  # classe-mãe dos usuários (comum e administrador)


def limpar_tela():  # limpa o terminal: 'cls' no Windows, 'clear' no Linux/macOS
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)


def pausar():  # espera o Enter antes de limpar a tela de novo
    input("\nPressione ENTER para voltar ao mural...")


def salvar_dados(usuarios, solicitacoes):  # objetos → dicionários → dados.json
    usuarios_dicts = {email: u.para_dict() for email, u in usuarios.items()}  # cada usuário vira dicionário
    solicitacoes_dicts = [s.para_dict() for s in solicitacoes]  # cada solicitação vira dicionário
    salvar(usuarios_dicts, solicitacoes_dicts)


def exibir_mural(solicitacoes, usuario_logado):  # tela inicial com o feed de solicitações
    print("=" * 65)
    print("  CIIU - Centro de Informação da Infraestrutura Universitária")
    if usuario_logado:
        print(f"  Perfil: {usuario_logado.perfil()}")  # cada tipo de usuário mostra o próprio perfil
    else:
        print("  Perfil: [Visitante]")
    print("=" * 65)

    ativas = [s for s in solicitacoes if s.esta_aberta()]  # Pendente ou Em andamento
    encerradas = [s for s in solicitacoes if not s.esta_aberta()]  # Concluída ou Recusada

    print("\n--- FEED DE SOLICITAÇÕES (ATIVAS) ---")
    if not ativas:
        print("  Nenhuma solicitação em pendência no momento.")
    else:
        for s in ativas:
            print(f"  #{s.id} [{s.natureza}] {s.titulo} | Local: {s.local} | "
                  f"Status: {s.status} | Prioridade: {s.calcular_prioridade()}")

    print("\n--- SOLICITAÇÕES ENCERRADAS ---")
    if not encerradas:
        print("  Nenhuma solicitação encerrada ainda.")
    else:
        for s in encerradas:
            print(f"  [{s.status}] #{s.id} [{s.natureza}] {s.titulo} ({s.local})")
    print("-" * 65)


def exigir_autenticacao(usuarios, solicitacoes):  # pede login ou cadastro quando precisa
    print("\n[!] Você precisa estar logado para realizar esta ação.")
    print("[1] Fazer Login")
    print("[2] Criar Conta (Cadastro)")
    print("[0] Voltar ao mural")
    escolha = input("Escolha: ").strip()

    if escolha == "1":
        if not usuarios:
            print("\nNenhum usuário cadastrado ainda. Crie uma conta primeiro!")
            return None
        return login_usuario(usuarios)  # devolve o objeto do usuário, ou None se errar 3 vezes

    if escolha == "2":
        cadastrar(usuarios)
        salvar_dados(usuarios, solicitacoes)  # salva o usuário novo na hora
        print("\nAgora faça login com sua nova conta:")
        return login_usuario(usuarios)

    return None  # escolheu voltar


def iniciar_menu(usuarios_dicts, solicitacoes_dicts):  # laço principal do programa
    usuarios = {email: Usuario.de_dict(email, d) for email, d in usuarios_dicts.items()}  # dicionários → objetos
    solicitacoes = [Solicitacao.de_dict(d) for d in solicitacoes_dicts]  # dicionários → objetos
    usuario_logado = None  # None = visitante; depois do login, guarda o OBJETO do usuário

    while True:
        limpar_tela()
        exibir_mural(solicitacoes, usuario_logado)
        admin = usuario_logado is not None and usuario_logado.eh_admin()  # True só para Administrador

        print("AÇÕES DISPONÍVEIS:")
        print("[1] Pesquisar")
        print("[2] Filtrar por departamento (#TAG)")
        print("[3] Nova solicitação")
        print("[4] Votar em prioridade (Enquete)")
        print("[5] Fazer Login / Cadastro" if not usuario_logado else "[5] Sair da conta")
        print("[6] Comentar em uma solicitação")
        print("[7] Ranking de prioridade")
        print("[8] Ver detalhes de uma solicitação")
        if usuario_logado:
            for linha in usuario_logado.opcoes_extras():  # polimorfismo: o comum não tem, o admin tem duas
                print(linha)
        print("[0] Fechar sistema")
        print("-" * 65)

        opcao = input("O que deseja fazer? ").strip()

        if opcao == "1":  # PESQUISAR (livre para visitantes)
            termo = input("Digite o termo de busca: ").lower().strip()
            resultados = [s for s in solicitacoes
                          if termo in s.titulo.lower() or termo in s.descricao.lower() or termo in s.local.lower()]
            print(f"\nEncontrado(s) {len(resultados)} resultado(s):")
            ver_solicitacoes(resultados, ver_autor_real=admin)
            pausar()

        elif opcao == "2":  # FILTRAR POR TAG (livre para visitantes)
            tag = input("Digite a tag do departamento (ex: #CEAGRI_2 ou #DEINFO): ").upper().strip()
            if not tag.startswith("#"):
                tag = "#" + tag
            filtradas = [s for s in solicitacoes
                         if s.autor in usuarios and usuarios[s.autor].tag() == tag]  # tag do curso de quem relatou
            print(f"\nSolicitações para {tag}:")
            ver_solicitacoes(filtradas, ver_autor_real=admin)
            pausar()

        elif opcao in ("3", "4", "6"):  # ações que exigem login
            if not usuario_logado:
                usuario_logado = exigir_autenticacao(usuarios, solicitacoes)
            if usuario_logado:
                limpar_tela()
                acoes = {"3": fazer_solicitacao, "4": votar_prioridade, "6": comentar}  # opção → função
                if acoes[opcao](solicitacoes, usuario_logado.email):  # True se algo mudou
                    salvar_dados(usuarios, solicitacoes)
            pausar()

        elif opcao == "5":  # LOGIN / CADASTRO OU SAIR
            if not usuario_logado:
                usuario_logado = exigir_autenticacao(usuarios, solicitacoes)
                pausar()
            else:
                print(f"Até logo, {usuario_logado.email}!")
                usuario_logado = None
                input("Pressione ENTER para continuar como visitante...")

        elif opcao == "7":  # RANKING (livre para visitantes)
            ver_ranking(solicitacoes)
            pausar()

        elif opcao == "8":  # DETALHES (livre; o admin vê o autor das anônimas)
            ver_detalhes(solicitacoes, ver_autor_real=admin)
            pausar()

        elif opcao == "9" and admin:  # ALTERAR STATUS (método do Administrador)
            limpar_tela()
            if usuario_logado.alterar_status(solicitacoes):
                salvar_dados(usuarios, solicitacoes)
            pausar()

        elif opcao == "10" and admin:  # VER USUÁRIOS (método do Administrador)
            usuario_logado.listar_usuarios(usuarios)
            pausar()

        elif opcao == "0":  # SAIR
            salvar_dados(usuarios, solicitacoes)
            print("Encerrando o CIIU...")
            break

        else:
            input("Opção inválida! Pressione ENTER...")
