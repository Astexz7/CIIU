from datetime import datetime  # usado para registrar a data e a hora de cada solicitação

NIVEIS = ("Alta", "Media", "Baixa")  # níveis de prioridade da enquete (sem acento, como são guardados)
PESOS = {"Alta": 3, "Media": 2, "Baixa": 1}  # peso de cada nível, usado para ordenar o ranking
STATUS_ENCERRADOS = ("Concluída", "Recusada")  # solicitações encerradas não recebem mais votos


class Solicitacao:  # classe-mãe: tudo o que toda solicitação tem
    natureza = "Geral"  # atributo de classe; cada subclasse troca este valor

    def __init__(self, id_solicitacao, autor, local, titulo, descricao, anonimo=False, foto=None):
        self.id = id_solicitacao  # número da solicitação (1, 2, 3...)
        self.autor = autor  # email de quem relatou (sempre salvo, mesmo se for anônimo)
        self.local = local  # onde está o problema
        self.titulo = titulo
        self.descricao = descricao
        self.anonimo = anonimo  # True = o nome não aparece para o público
        self.foto = foto  # caminho da foto, ou None
        self.data = datetime.now().strftime("%d/%m/%Y %H:%M")  # quando foi criada
        self.status = "Pendente"  # toda solicitação começa como Pendente
        self.votos = {"Alta": 0, "Media": 0, "Baixa": 0}  # contagem da enquete de prioridade
        self.votantes = []  # emails de quem já votou (cada pessoa vota uma vez)
        self.historico = []  # mudanças de status feitas pelo administrador
        self.comentarios = []  # comentários da comunidade

    @classmethod
    def exemplos(cls):  # método de classe: cada natureza mostra exemplos diferentes
        return ""

    def total_votos(self):  # quantas pessoas já votaram
        return sum(self.votos.values())

    def pontuacao(self):  # média ponderada dos votos (Alta=3, Média=2, Baixa=1); 0 se ninguém votou
        total = self.total_votos()
        if total == 0:
            return 0
        return sum(PESOS[nivel] * qtd for nivel, qtd in self.votos.items()) / total

    def calcular_prioridade(self):  # resultado da enquete em texto, ex: "Alta (67%)"
        total = self.total_votos()
        if total == 0:
            return "Sem votos"
        maior = max(self.votos.values())  # quantidade de votos do nível mais votado
        vencedores = [nivel for nivel in NIVEIS if self.votos[nivel] == maior]  # pode haver empate
        porcentagem = (maior / total) * 100
        if len(vencedores) > 1:  # dois ou três níveis com a mesma quantidade de votos
            return f"Empate {'/'.join(vencedores)} ({porcentagem:.0f}% cada)"
        return f"{vencedores[0]} ({porcentagem:.0f}%)"

    def autor_visivel(self, ver_autor_real=False):  # o que mostrar no lugar do autor
        if self.anonimo and not ver_autor_real:  # anônima e quem está vendo não é admin
            return "Anônimo"
        if self.anonimo:  # anônima, mas quem está vendo é admin
            return f"{self.autor} (anônimo para o público)"
        return self.autor

    def esta_aberta(self):  # True se ainda pode receber votos
        return self.status not in STATUS_ENCERRADOS

    def para_dict(self):  # transforma o objeto em dicionário, para salvar no dados.json
        return {
            "id": self.id,
            "autor": self.autor,
            "local": self.local,
            "natureza": self.natureza,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "anonimo": self.anonimo,
            "foto": self.foto,
            "data": self.data,
            "status": self.status,
            "votos": self.votos,
            "votantes": self.votantes,
            "historico": self.historico,
            "comentarios": self.comentarios,
        }

    @classmethod
    def de_dict(cls, d):  # faz o caminho contrário: dicionário do dados.json → objeto da classe certa
        mapa_classes = {
            "Estrutural": SolicitacaoEstrutural,
            "Eletrônico": SolicitacaoEletronico,
            "Uso Geral": SolicitacaoUsoGeral,
        }
        classe_certa = mapa_classes.get(d.get("natureza"), Solicitacao)  # natureza desconhecida → classe-mãe
        obj = classe_certa(
            d.get("id", 1),
            d["autor"],
            d["local"],
            d["titulo"],
            d["descricao"],
            d.get("anonimo", False),  # .get com valor padrão: dados antigos continuam funcionando
            d.get("foto"),
        )
        obj.data = d.get("data", "")
        obj.status = d.get("status", "Pendente")
        votos = d.get("votos", {})
        if set(votos) == set(NIVEIS):  # só aproveita votos no formato Alta/Media/Baixa
            obj.votos = votos
        obj.votantes = d.get("votantes", [])
        obj.historico = d.get("historico", [])
        obj.comentarios = d.get("comentarios", [])
        return obj


class SolicitacaoEstrutural(Solicitacao):  # herança: tem tudo da Solicitacao, só muda a natureza
    natureza = "Estrutural"

    @classmethod
    def exemplos(cls):
        return "paredes, teto, janelas, piso"


class SolicitacaoEletronico(Solicitacao):
    natureza = "Eletrônico"

    @classmethod
    def exemplos(cls):
        return "computador, internet, luz, projetor, ar-condicionado"


class SolicitacaoUsoGeral(Solicitacao):
    natureza = "Uso Geral"

    @classmethod
    def exemplos(cls):
        return "cadeiras, quadros, mesas, privadas, bebedouros"


def pedir_texto(pergunta):  # repete a pergunta até o usuário digitar algo
    while True:
        texto = input(pergunta).strip()
        if texto:  # texto vazio conta como False
            return texto
        print("Este campo não pode ficar vazio.")


def fazer_solicitacao(solicitacoes, usuario_logado):  # cria uma solicitação e coloca na lista
    classes_natureza = {  # cada opção do menu aponta para uma subclasse
        '1': SolicitacaoEstrutural,
        '2': SolicitacaoEletronico,
        '3': SolicitacaoUsoGeral,
    }

    print('Qual a natureza do problema?')
    for chave, classe in classes_natureza.items():
        print(f"[{chave}] {classe.natureza} (Ex: {classe.exemplos()})")  # polimorfismo: cada classe tem seus exemplos

    op_nat = input('Escolha uma opção: ').strip()
    if op_nat not in classes_natureza:
        print('Opção inválida.')
        return False

    local = pedir_texto('Local do problema (ex: Biblioteca, DECON, CEAGRI): ')
    titulo = pedir_texto('Título resumido do problema: ')
    descricao = pedir_texto('Descreva o problema: ')
    foto = input('Caminho da foto (Enter para pular): ').strip() or None  # opcional
    anonimo = input('Deseja ficar anônimo? (s/n): ').strip().lower() == 's'

    proximo_id = max((s.id for s in solicitacoes), default=0) + 1  # próximo número livre
    classe_escolhida = classes_natureza[op_nat]
    solicitacao = classe_escolhida(proximo_id, usuario_logado, local, titulo, descricao, anonimo, foto)  # cria o objeto

    solicitacoes.append(solicitacao)
    print('Solicitação registrada! Obrigado por sua contribuição, a UFRPE agradece.')
    return True


def ver_solicitacoes(solicitacoes, ver_autor_real=False):  # lista resumida (usada na pesquisa e no filtro)
    if not solicitacoes:
        print('Nenhuma solicitação encontrada.')
        return
    for s in solicitacoes:
        print(
            f"#{s.id} | {s.titulo} [{s.natureza}] | Local: {s.local} | "
            f"Autor: {s.autor_visivel(ver_autor_real)} | Status: {s.status} | "
            f"Prioridade: {s.calcular_prioridade()}"
        )


def buscar_por_id(solicitacoes, numero):  # devolve a solicitação com esse número, ou None
    for s in solicitacoes:
        if s.id == numero:
            return s
    return None


def ver_detalhes(solicitacoes, ver_autor_real=False):  # mostra tudo sobre uma solicitação
    numero = input('Número da solicitação (#): ').strip().lstrip('#')
    s = buscar_por_id(solicitacoes, int(numero)) if numero.isdigit() else None
    if s is None:
        print('Solicitação não encontrada.')
        return

    print("-" * 65)
    print(f"#{s.id} - {s.titulo}  [{s.natureza}]  [{s.status}]")
    print(f"Local: {s.local} | Autor: {s.autor_visivel(ver_autor_real)} | Data: {s.data}")
    print(f"Descrição: {s.descricao}")
    if s.foto:
        print(f"Foto: {s.foto}")
    print(f"Enquete: Alta {s.votos['Alta']} | Média {s.votos['Media']} | Baixa {s.votos['Baixa']}"
          f"  →  Prioridade: {s.calcular_prioridade()}")
    for h in s.historico:  # mudanças de status
        print(f"  ↳ {h['data']}: {h['de']} → {h['para']}")
    for c in s.comentarios:  # comentários da comunidade
        print(f"  💬 {c['autor']} ({c['data']}): {c['texto']}")
    print("-" * 65)
