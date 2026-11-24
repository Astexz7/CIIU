import subprocess
import os
from cadastro import cadastrar
from login import login_usuario
from dados import salvar
from admin import eh_admin, alterar_status
from solicitacoes import (
    Solicitacao,
    fazer_solicitacao,
    ver_solicitacoes,
    votar_prioridade,
)


def limpar_tela():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)


def salvar_dados(usuarios, solicitacoes_obj, solicitacoes_originais):
    dicts = [s.para_dict() for s in solicitacoes_obj]
    solicitacoes_originais[:] = dicts
    salvar(usuarios, dicts)


def exibir_mural(solicitacoes, usuario_logado, usuarios):
    print("=" * 65)
    print("  [BRASÃO UFRPE] CIIU - Centro de Info. da Infraestrutura Univ.")
    if usuario_logado:
        curso_tag = usuarios[usuario_logado]['curso']['tag']
        cargo = " [ADMIN]" if eh_admin(usuario_logado) else ""
        print(f"  Perfil: {usuario_logado} ({curso_tag}){cargo}")
    else:
        print("  Perfil: [Visitante]")
    print("=" * 65)

    ativas = [s for s in solicitacoes if s.status != 'Concluída']
    concluidas = [s for s in solicitacoes if s.status == 'Concluída']

    print("\n--- FEED DE SOLICITAÇÕES (ATIVAS) ---")
    if not ativas:
        print("  Nenhuma solicitação em pendência no momento.")
    else:
        for i, s in enumerate(ativas, start=1):
            print(f"  [{i}] #{s.id} [{s.natureza}] {s.titulo} - {s.descricao} | Local: {s.local} | Status: {s.status} | Prioridade: {s.calcular_prioridade()}")

    print("\n--- SOLICITAÇÕES CONCLUÍDAS ---")
    if not concluidas:
        print("  Nenhuma solicitação concluída ainda.")
    else:
        for s in concluidas:
            print(f"  [Concluída] #{s.id} [{s.natureza}] {s.titulo} - {s.descricao} ({s.local})")
    print("-" * 65)


def iniciar_menu(usuarios, solicitacoes_dicts):
    usuario_logado = None
    solicitacoes = [Solicitacao.de_dict(d) for d in solicitacoes_dicts]

    while True:
        limpar_tela()
        exibir_mural(solicitacoes, usuario_logado, usuarios)

        print("AÇÕES DISPONÍVEIS:")
        print("[1] Pesquisar (Barra de busca)")
        print("[2] Filtrar por departamento (#TAG)")
        print("[3] Nova solicitação (Ícone de Lápis)")
        print("[4] Votar em prioridade (Enquete)")
        if not usuario_logado:
            print("[5] Fazer Login / Cadastro")
        else:
            print("[5] Sair da conta (Deslogar)")
            if eh_admin(usuario_logado):
                print("[6] Alterar status de solicitação (Admin)")
        print("[0] Fechar sistema")
        print("-" * 65)

        opcao = input("O que deseja fazer? ").strip()

        # 1. PESQUISAR (Livre para visitantes)
        if opcao == "1":
            termo = input("Digite o termo de busca: ").lower().strip()
            resultados = [
                s for s in solicitacoes
                if termo in s.descricao.lower() or termo in s.titulo.lower()
            ]
            print(f"\nEncontrado(s) {len(resultados)} resultado(s):")
            ver_solicitacoes(resultados)
            input("\nPressione ENTER para voltar...")

        # 2. FILTRAR (Livre para visitantes)
        elif opcao == "2":
            tag = input("Digite a tag do departamento (ex: #CEAGRI_2 ou #DEINFO): ").upper().strip()
            if not tag.startswith("#"):
                tag = "#" + tag
            filtradas = [
                s for s in solicitacoes
                if usuarios.get(s.autor, {}).get('curso', {}).get('tag') == tag
            ]
            print(f"\nSolicitações para {tag}:")
            ver_solicitacoes(filtradas)
            input("\nPressione ENTER para voltar...")

        # 3. NOVA SOLICITAÇÃO (Exige login)
        elif opcao == "3":
            if not usuario_logado:
                usuario_logado = exigir_autenticacao(usuarios, solicitacoes, solicitacoes_dicts)

            if usuario_logado:
                limpar_tela()
                if fazer_solicitacao(solicitacoes, usuarios, usuario_logado):
                    salvar_dados(usuarios, solicitacoes, solicitacoes_dicts)
                input("\nPressione ENTER para voltar ao mural...")

        # 4. VOTAR NA PRIORIDADE (Exige login)
        elif opcao == "4":
            if not usuario_logado:
                usuario_logado = exigir_autenticacao(usuarios, solicitacoes, solicitacoes_dicts)

            if usuario_logado:
                limpar_tela()
                if votar_prioridade(solicitacoes, usuario_logado):
                    salvar_dados(usuarios, solicitacoes, solicitacoes_dicts)
                input("\nPressione ENTER para voltar ao mural...")

        # 5. LOGIN / CADASTRO OU LOGOUT
        elif opcao == "5":
            if not usuario_logado:
                usuario_logado = exigir_autenticacao(usuarios, solicitacoes, solicitacoes_dicts)
            else:
                print(f"Até logo, {usuario_logado}!")
                usuario_logado = None
                input("Pressione ENTER para continuar como visitante...")

        # 6. ALTERAR STATUS (ADMIN)
        elif opcao == "6" and usuario_logado and eh_admin(usuario_logado):
            limpar_tela()
            dicts_temp = [s.para_dict() for s in solicitacoes]
            if alterar_status(dicts_temp, usuario_logado):
                solicitacoes = [Solicitacao.de_dict(d) for d in dicts_temp]
                salvar_dados(usuarios, solicitacoes, solicitacoes_dicts)
            input("\nPressione ENTER para voltar ao mural...")

        # 0. SAIR
        elif opcao == "0":
            salvar_dados(usuarios, solicitacoes, solicitacoes_dicts)
            print("Encerrando o CIIU...")
            break
        else:
            input("Opção inválida! Pressione ENTER...")


def exigir_autenticacao(usuarios, solicitacoes, solicitacoes_dicts):
    print("\n[!] Você precisa estar logado para realizar esta ação.")
    print("[1] Fazer Login")
    print("[2] Criar Conta (Cadastro)")
    print("[0] Voltar ao mural")
    escolha = input("Escolha: ").strip()

    if escolha == "1":
        if not usuarios:
            input("\nNenhum usuário cadastrado ainda. Crie uma conta primeiro! (Pressione ENTER para retornar ao mural)")
            return None
        return login_usuario(usuarios)

    elif escolha == "2":
        cadastrar(usuarios)
        salvar_dados(usuarios, solicitacoes, solicitacoes_dicts)
        print("\nAgora faça login com sua nova conta:")
        return login_usuario(usuarios)

    return None
