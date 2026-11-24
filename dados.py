import json  # biblioteca para transformar dicionários/listas em texto (e o contrário)
from pathlib import Path  # classe para trabalhar com caminhos de arquivos

ARQUIVO = Path("dados.json")  # nome do arquivo onde tudo fica salvo (na mesma pasta do programa)


def carregar():  # lê os dados salvos quando o programa abre
    """Lê usuários e solicitações do arquivo. Se não existir, começa vazio."""
    if ARQUIVO.exists():  # se o arquivo já existe (o programa já foi usado antes)...
        dados = json.loads(ARQUIVO.read_text(encoding="utf-8"))  # ...lê o texto do arquivo e transforma em dicionário
        return dados["usuarios"], dados["solicitacoes"]  # devolve as duas coisas separadas
    return {}, []  # primeira vez: devolve dicionário de usuários vazio e lista de solicitações vazia


def salvar(usuarios, solicitacoes):  # grava os dados no arquivo
    """Grava usuários e solicitações no arquivo."""
    ARQUIVO.write_text(  # escreve (e substitui) o conteúdo do arquivo
        json.dumps({"usuarios": usuarios, "solicitacoes": solicitacoes},  # junta tudo num dicionário e converte para texto JSON
                   ensure_ascii=False, indent=2),  # ensure_ascii=False mantém os acentos; indent=2 deixa o arquivo legível
        encoding="utf-8",  # salva com acentuação correta
    )
