from datetime import datetime  # usado para pegar a data e a hora atuais


def pedir_texto(pergunta):  # função de apoio: pergunta algo e não aceita resposta vazia
    """Repete a pergunta até o usuário digitar algo."""
    while True:  # repete até dar "return"
        texto = input(pergunta).strip()  # lê a resposta e tira espaços do começo e do fim
        if texto:  # texto vazio conta como False; qualquer coisa escrita conta como True
            return texto  # devolve a resposta
        print("Este campo não pode ficar vazio.")  # se estava vazio, avisa e pergunta de novo


def fazer_solicitacao(solicitacoes, usuario_logado):  # recebe a lista de solicitações e o email de quem está logado
    titulo = pedir_texto("Título: ")  # título curto do problema (obrigatório)
    descricao = pedir_texto("Descreva o problema: ")  # explicação do problema (obrigatória)
    local = pedir_texto("Local (ex: Bloco B, sala 12): ")  # onde fica o problema (obrigatório)
    foto = input("Caminho da foto (Enter para pular): ").strip() or None  # opcional; se ficar vazio, "or None" guarda None
    anonimo = input("Deseja ficar anônimo? (s/n): ").strip().lower() == "s"  # vira True se digitar "s", senão False

    solicitacoes.append({  # adiciona um dicionário novo no final da lista
        "id": len(solicitacoes) + 1,  # número da solicitação (1, 2, 3...)
        "titulo": titulo,
        "descricao": descricao,
        "local": local,
        "foto": foto,
        "autor": usuario_logado,  # sempre salvo, mesmo se for anônimo
        "anonimo": anonimo,  # True ou False; decide se o nome aparece na listagem
        "status": "Pendente",  # toda solicitação começa como Pendente
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),  # data e hora de agora no formato 24/11/2026 17:19
    })  # fim do dicionário
    print("Solicitação registrada!")  # avisa que deu certo


def ver_solicitacoes(solicitacoes, ver_autor_real=False):  # ver_autor_real=True só para o administrador
    if not solicitacoes:  # lista vazia conta como False; "not" inverte para True
        print('Nenhuma solicitação ainda.')  # avisa que não tem nada
        return  # sai da função sem fazer mais nada

    for s in solicitacoes:  # percorre a lista; "s" é uma solicitação (um dicionário) por vez
        if s["anonimo"] and not ver_autor_real:  # anônima e quem está vendo não é admin...
            autor = "Anônimo"  # ...esconde o nome
        elif s["anonimo"]:  # anônima, mas quem está vendo é admin...
            autor = f"{s['autor']} (anônimo para o público)"  # ...mostra o email com um aviso
        else:  # não é anônima
            autor = s["autor"]  # mostra o email normalmente
        print("-" * 50)  # linha separadora com 50 tracinhos
        print(f"#{s['id']} - {s['titulo']}  [{s['status']}]")  # ex: #1 - Ar quebrado  [Pendente]
        print(f"Local: {s['local']} | Autor: {autor} | Data: {s['data']}")  # local, autor e data
        print(f"Descrição: {s['descricao']}")  # descrição do problema
        if s["foto"]:  # só mostra a foto se tiver uma (None conta como False)
            print(f"Foto: {s['foto']}")
        for h in s.get("historico", []):  # .get devolve [] se a solicitação ainda não tem histórico
            print(f"  ↳ {h['data']}: {h['de']} → {h['para']}")  # ex: ↳ 25/11/2026 10:00: Pendente → Em andamento
    print("-" * 50)  # linha separadora final
