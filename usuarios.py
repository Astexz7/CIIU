from datetime import datetime  # usado para registrar a data de cada mudança de status

from seguranca import conferir_senha  # confere a senha digitada com o hash salvo
from solicitacoes import buscar_por_id  # procura uma solicitação pelo número

ADMINS = {"festo.murilo@ufrpe.br"}  # emails de administrador (para adicionar mais, separe com vírgula)

STATUS_POSSIVEIS = ["Pendente", "Em andamento", "Concluída", "Recusada"]  # "Recusada" = fora do escopo do projeto


class Usuario:  # classe-mãe: tudo o que todo usuário tem
    tipo = "Usuário"  # atributo de classe; cada subclasse troca este valor

    def __init__(self, email, senha_hash, curso):
        self.email = email  # email institucional (é também a "chave" do usuário)
        self.senha_hash = senha_hash  # senha já transformada em hash (nunca a senha de verdade)
        self.curso = curso  # dicionário com o nome do curso e a tag do departamento

    def tag(self):  # tag do departamento do curso, ex: #DEINFO
        return self.curso.get("tag", "")

    def senha_correta(self, senha):  # True se a senha digitada bate com o hash salvo
        return conferir_senha(senha, self.senha_hash)

    def eh_admin(self):  # usuário comum não é administrador (o Administrador sobrescreve)
        return False

    def perfil(self):  # texto mostrado no topo do mural
        return f"{self.email} ({self.tag()}) - {self.tipo}"

    def opcoes_extras(self):  # opções a mais no menu; o usuário comum não tem nenhuma
        return []

    def para_dict(self):  # objeto → dicionário, para salvar no dados.json
        return {"tipo": self.tipo, "senha": self.senha_hash, "curso": self.curso}

    @classmethod
    def de_dict(cls, email, d):  # dicionário do dados.json → objeto da subclasse certa
        return criar_usuario(email, d["senha"], d["curso"])


class UsuarioComum(Usuario):  # herança: aluno, professor ou servidor sem poderes de administrador
    tipo = "Usuário comum"


class Administrador(Usuario):  # herança: tem tudo do Usuario e ganha poderes extras
    tipo = "Administrador"

    def eh_admin(self):  # sobrescreve o método da classe-mãe (polimorfismo)
        return True

    def opcoes_extras(self):  # o administrador vê duas opções a mais no menu
        return ["[9] Alterar status de solicitação (Admin)",
                "[10] Ver usuários cadastrados (Admin)"]

    def alterar_status(self, solicitacoes):  # muda o status de uma solicitação e registra no histórico
        if not solicitacoes:
            print("Nenhuma solicitação para alterar.")
            return False

        print("\nSolicitações:")
        for s in solicitacoes:
            print(f"#{s.id} - {s.titulo}  [{s.status}]")

        numero = input("Digite o número da solicitação: ").strip().lstrip('#')
        if not numero.isdigit():
            print("Número inválido.")
            return False

        s = buscar_por_id(solicitacoes, int(numero))
        if s is None:
            print("Solicitação não encontrada.")
            return False

        print(f"Status atual: {s.status}")
        for i, status in enumerate(STATUS_POSSIVEIS, start=1):  # enumerate numera as opções: 1, 2, 3, 4
            print(f"{i} - {status}")

        escolha = input("Novo status: ").strip()
        if not escolha.isdigit() or not 1 <= int(escolha) <= len(STATUS_POSSIVEIS):
            print("Opção inválida.")
            return False

        novo_status = STATUS_POSSIVEIS[int(escolha) - 1]  # -1 porque a lista começa no índice 0
        if novo_status == s.status:
            print("A solicitação já está com esse status.")
            return False

        s.historico.append({  # transparência: toda mudança fica registrada
            "de": s.status,
            "para": novo_status,
            "por": self.email,  # o próprio administrador que está fazendo a mudança
            "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        })
        s.status = novo_status
        print(f"Status alterado para: {novo_status}")
        return True

    def listar_usuarios(self, usuarios):  # mostra todos os usuários e o tipo de cada um
        print("\n===== USUÁRIOS CADASTRADOS =====")
        ordenados = sorted(usuarios.values(), key=lambda u: (not u.eh_admin(), u.email))  # administradores primeiro
        for u in ordenados:
            print(f"  {u.perfil()}")  # polimorfismo: cada objeto mostra o próprio tipo
        admins = sum(1 for u in usuarios.values() if u.eh_admin())
        print(f"\nTotal: {len(usuarios)} usuário(s) | {admins} administrador(es) | "
              f"{len(usuarios) - admins} usuário(s) comum(ns)")


def criar_usuario(email, senha_hash, curso):  # decide qual subclasse usar pelo email
    classe = Administrador if email in ADMINS else UsuarioComum
    return classe(email, senha_hash, curso)
