from datetime import datetime  # usado para registrar a data de cada comentário

from solicitacoes import buscar_por_id, pedir_texto  # funções de apoio que já existem no solicitacoes.py

OPCOES_VOTO = {'1': 'Alta', '2': 'Media', '3': 'Baixa'}  # opção digitada → nível guardado


def votar_prioridade(solicitacoes, usuario_logado):  # enquete: o aluno vota se a prioridade é Alta, Média ou Baixa
    ativas = [s for s in solicitacoes if s.esta_aberta()]  # Concluída e Recusada não recebem votos

    if not ativas:
        print('Nenhuma solicitação ativa para votar.')
        return False

    for i, s in enumerate(ativas, start=1):  # lista numerada só com as abertas
        print(f"[{i}] #{s.id} {s.titulo} ({s.local}) - Prioridade: {s.calcular_prioridade()}")

    escolha = input('\nEscolha o número da solicitação para votar: ').strip()
    if not (escolha.isdigit() and 1 <= int(escolha) <= len(ativas)):  # precisa ser um número da lista
        print('Número inválido.')
        return False

    s = ativas[int(escolha) - 1]  # -1 porque a lista começa no índice 0

    if usuario_logado in s.votantes:  # cada pessoa vota UMA vez por solicitação
        print('Você já votou na prioridade desta solicitação!')
        print(f'Resultado atual: {s.calcular_prioridade()}')  # mostra só o resultado
        return False

    print('[1] Alta | [2] Média | [3] Baixa')
    voto = input('Qual o nível de prioridade? ').strip()
    if voto not in OPCOES_VOTO:
        print('Opção inválida. Selecione 1, 2 ou 3.')
        return False

    nivel = OPCOES_VOTO[voto]
    s.votos[nivel] += 1  # soma um voto no nível escolhido
    s.votantes.append(usuario_logado)  # guarda quem votou, para não votar de novo
    print(f'Voto "{nivel}" registrado! Prioridade atual: {s.calcular_prioridade()}')
    return True  # avisa o menu para salvar


def comentar(solicitacoes, usuario_logado):  # adiciona um comentário a uma solicitação
    numero = input('Número da solicitação (#) para comentar: ').strip().lstrip('#')
    s = buscar_por_id(solicitacoes, int(numero)) if numero.isdigit() else None
    if s is None:
        print('Solicitação não encontrada.')
        return False

    texto = pedir_texto('Seu comentário: ')  # não aceita comentário vazio
    s.comentarios.append({
        "autor": usuario_logado,
        "texto": texto,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
    })
    print('Comentário adicionado!')
    return True  # avisa o menu para salvar


def ver_ranking(solicitacoes):  # solicitações abertas da mais prioritária para a menos prioritária
    ativas = [s for s in solicitacoes if s.esta_aberta()]
    if not ativas:
        print('Nenhuma solicitação aberta.')
        return

    ordenadas = sorted(  # ordena pela pontuação da enquete; no empate, pela quantidade de votos
        ativas,
        key=lambda s: (s.pontuacao(), s.total_votos()),  # lambda = função curta de uma linha
        reverse=True,  # da maior prioridade para a menor
    )

    print("\n===== RANKING DE PRIORIDADE =====")
    for posicao, s in enumerate(ordenadas, start=1):  # 1º, 2º, 3º...
        print(f"{posicao}º  #{s.id} - {s.titulo} ({s.local})  |  {s.calcular_prioridade()}"
              f"  |  {s.total_votos()} voto(s)  [{s.status}]")
