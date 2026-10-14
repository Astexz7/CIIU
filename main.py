from cadastro import cadastrar
from login import login_usuario

usuarios = {}
solicitacoes = []
cadastrar(usuarios)

usuario_logado= login_usuario(usuarios)
print(f'Usuário logado: {usuario_logado}')
