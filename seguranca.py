import hashlib  # biblioteca do Python que cria "hashes" (códigos embaralhados que não dá para desfazer)
import hmac  # biblioteca usada aqui para comparar os hashes de forma segura
import os  # biblioteca do sistema; usamos para gerar bytes aleatórios


def gerar_hash(senha):  # recebe a senha digitada e devolve o texto que vai ser guardado
    """Transforma a senha em um hash seguro para guardar."""
    sal = os.urandom(16)  # gera 16 bytes aleatórios (o "sal"); assim duas senhas iguais viram hashes diferentes
    h = hashlib.pbkdf2_hmac("sha256", senha.encode(), sal, 200_000)  # embaralha a senha junto com o sal 200 mil vezes (fica lento para quem tenta adivinhar)
    return sal.hex() + ":" + h.hex()  # converte sal e hash para texto e junta os dois com ":" no meio


def conferir_senha(senha, guardado):  # recebe a senha digitada no login e o texto guardado no cadastro
    """Confere se a senha digitada bate com o hash guardado."""
    sal_hex, h_hex = guardado.split(":")  # separa o texto guardado em duas partes: o sal e o hash
    h = hashlib.pbkdf2_hmac("sha256", senha.encode(), bytes.fromhex(sal_hex), 200_000)  # refaz o hash da senha digitada usando o MESMO sal do cadastro
    return hmac.compare_digest(h.hex(), h_hex)  # compara os dois hashes; True se forem iguais (senha certa), False se não
