from cadastro import cadastrar
from login import login_usuario
from solicitacoes import fazer_solicitacao, ver_solicitacoes

usuarios = {}
solicitacoes = []
cadastrar(usuarios)

usuario_logado= login_usuario(usuarios)
print(f'Usuário logado: {usuario_logado}')

fazer_solicitacao(solicitacoes, usuarios, usuario_logado)  # chama a função com os 3 dados que ela precisa
ver_solicitacoes(solicitacoes)  # chama a função que mostra todas