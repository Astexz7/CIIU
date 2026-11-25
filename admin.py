from datetime import datetime  # usado para registrar a data e a hora de cada mudança de status

ADMINS = {"festo.murilo@ufrpe.br"}  # emails que têm permissão de administrador (para adicionar mais, separe com vírgula)

STATUS_POSSIVEIS = ["Pendente", "Em andamento", "Concluída", "Recusada"]  # "Recusada" = fora do escopo do projeto, após a revisão da equipe


def eh_admin(email):  # recebe o email de quem está logado
    """Diz se o email pertence a um administrador."""
    return email in ADMINS  # True se o email estiver na lista ADMINS, False se não


def buscar_solicitacao(solicitacoes, numero):  # procura uma solicitação pelo número (id)
    """Devolve a solicitação com esse id, ou None se não existir."""
    for s in solicitacoes:  # percorre a lista, uma solicitação por vez
        if s["id"] == numero:  # achou a solicitação com esse número?
            return s  # devolve ela
    return None  # percorreu tudo e não achou


def alterar_status(solicitacoes, admin_logado):  # recebe a lista e o email do administrador
    """Muda o status de uma solicitação. Retorna True se algo mudou."""
    if not solicitacoes:  # lista vazia
        print("Nenhuma solicitação para alterar.")
        return False  # nada mudou

    print("\nSolicitações:")  # mostra uma lista resumida para o admin escolher
    for s in solicitacoes:  # percorre todas
        print(f"#{s['id']} - {s['titulo']}  [{s['status']}]")  # ex: #1 - Ar quebrado  [Pendente]

    numero = input("Digite o número da solicitação: ").strip()  # lê o número como texto
    if not numero.isdigit():  # se não for só número...
        print("Número inválido.")
        return False

    s = buscar_solicitacao(solicitacoes, int(numero))  # procura a solicitação escolhida
    if s is None:  # não existe solicitação com esse número
        print("Solicitação não encontrada.")
        return False

    print(f"Status atual: {s['status']}")  # mostra como está agora
    for i, status in enumerate(STATUS_POSSIVEIS, start=1):  # enumerate numera a lista: 1, 2, 3
        print(f"{i} - {status}")  # ex: 2 - Em andamento

    escolha = input("Novo status: ").strip()  # lê a escolha como texto
    if not escolha.isdigit() or not 1 <= int(escolha) <= len(STATUS_POSSIVEIS):  # precisa ser um número da lista (1 a 4)
        print("Opção inválida.")
        return False

    novo_status = STATUS_POSSIVEIS[int(escolha) - 1]  # -1 porque a lista começa no índice 0
    if novo_status == s["status"]:  # escolheu o mesmo status que já estava
        print("A solicitação já está com esse status.")
        return False

    s.setdefault("historico", []).append({  # cria a lista "historico" se ainda não existir e adiciona um registro
        "de": s["status"],  # status antigo
        "para": novo_status,  # status novo
        "por": admin_logado,  # quem mudou
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),  # quando mudou
    })
    s["status"] = novo_status  # troca o status de verdade
    print(f"Status alterado para: {novo_status}")
    return True  # avisa o main que algo mudou (para ele salvar)
