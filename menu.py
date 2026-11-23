def exigir_autenticacao(usuarios):
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
        print("\nAgora faça login com sua nova conta:")
        return login_usuario(usuarios)
    
    return None
