def fazer_solicitacao(solicitacoes, usuarios, usuario_logado):  # recebe a lista, os usuários e o email de quem logou
    local = usuarios[usuario_logado]['curso']['curso']  # entra no usuário, depois no dicionário do curso, e pega o nome do curso
    print(f'Local da solicitação: {local}')  # mostra o local, que é o curso do aluno
    descricao = input('Descreva o problema: ')  # o usuário digita o problema e a variável guarda o texto

    solicitacao = {'autor': usuario_logado, 'local': local, 'descricao': descricao}  # dicionário pequeno com as 3 informações
    solicitacoes.append(solicitacao)  # coloca o dicionário no final da lista
    print('Solicitação registrada!')  # avisa que deu certo


def ver_solicitacoes(solicitacoes):  # recebe só a lista
    if len(solicitacoes) == 0:  # len conta os itens; 0 significa lista vazia
        print('Nenhuma solicitação ainda.')  # trata o caso da lista vazia
    else:
        for s in solicitacoes:  # percorre a lista, e s é um dicionário por vez
            print(f"Autor: {s['autor']} | Local: {s['local']} | Descrição: {s['descricao']}")  # busca cada valor pela chaves