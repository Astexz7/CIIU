<div align="center">

# 🏛️ CIIU

### Centro de Informação da Infraestrutura Universitária

*Um canal único para a comunidade da UFRPE reportar problemas de infraestrutura no campus, votar na prioridade de cada um e acompanhar até quando eles são resolvidos.*

[Sobre](#-sobre-o-projeto) •
[Como funciona](#-como-funciona) •
[Inovação](#-inovação) •
[Releases](#-releases) •
[Requisitos](#-requisitos-e-importações) •
[Como rodar](#️-como-rodar) •
[Bibliotecas](#-bibliotecas-utilizadas) •
[Módulos](#-organização-dos-módulos) •
[Dados](#-como-os-dados-são-guardados) •
[Equipe](#-equipe)

</div>

---

## 💡 Sobre o projeto

Ar-condicionado quebrado, banheiro sem manutenção, bebedouro parado, lâmpada queimada. Quase todo aluno já viu um problema desses, mas poucos sabem a quem avisar, e quem avisa raramente descobre se alguma coisa foi feita.

O CIIU reúne esses relatos em um só lugar, com **participação da comunidade** (enquete de prioridade e comentários) e **transparência** no andamento de cada solicitação.

A versão atual é um **protótipo em linha de comando (terminal)**, escrito em Python 3, que implementa todas as regras do sistema. A interface web está prevista para as próximas etapas.

---

## ✨ Como funciona

| Passo | O que acontece |
|:---:|---|
| **1** | 👤 O aluno cria uma conta com email `@ufrpe.br`, confirmado por um código enviado por email |
| **2** | 📝 Registra um problema escolhendo a natureza (Estrutural, Eletrônico ou Uso Geral), com título, descrição, local e foto (opcional) |
| **3** | 🕶️ Pode marcar o registro como anônimo: o nome fica oculto para o público |
| **4** | 📰 Todos, até visitantes, veem o mural, pesquisam e filtram por departamento |
| **5** | 🗳️ A comunidade vota na enquete de prioridade (Alta, Média ou Baixa) e comenta |
| **6** | 🏆 O ranking mostra os problemas abertos do mais prioritário para o menos prioritário |
| **7** | 📊 O administrador atualiza o status, e cada mudança fica no histórico |

```
🟡 Pendente   ➜   🔵 Em andamento   ➜   🟢 Concluída

🔴 Recusada  (quando o problema está fora do escopo do projeto)
```

> 🔒 **Sobre o anonimato:** ele é apenas de exibição. O autor continua salvo nos dados, mas não aparece para o público. Só o administrador consegue ver.

---

## 🚀 Inovação

O diferencial do CIIU em relação a sistemas de chamados de manutenção é transformar reclamações individuais em **prioridades coletivas**:

- **Enquete de prioridade (Alta, Média ou Baixa):** cada pessoa vota **uma vez por solicitação**; quem já votou vê apenas o resultado atual. O resultado aparece com a porcentagem do nível mais votado, por exemplo `Alta (67%)`, e empates são mostrados como `Empate Alta/Baixa`.
- **Ranking de prioridade:** as solicitações abertas são ordenadas por uma média ponderada dos votos (Alta = 3, Média = 2, Baixa = 1) e, em caso de empate, pelo número de votos (`sorted` com `key=lambda`).
- **Transparência:** cada mudança de status fica registrada num histórico (de qual status, para qual, por quem e quando) que todos podem ver.
- **Acesso restrito à comunidade:** só entra quem confirma um email `@ufrpe.br` pelo código de verificação.
- **Anonimato de exibição:** o aluno pode relatar sem se expor, sem que o relato perca a rastreabilidade.

---

## 🗂️ Releases

| Release | Foco | Entregas |
|:---:|---|---|
| **1.0** | Base do sistema | Cadastro de usuários, cursos, login e solicitações |
| **2.0** | Segurança, acompanhamento e comunidade | Mural com menu, classes (orientação a objetos), senhas com hash e asteriscos, dados salvos em arquivo, anonimato, pesquisa e filtro, status com histórico, administrador, enquete de prioridade, ranking e comentários |
| **2.1** | Usuários como classes | Classe-mãe `Usuario` com as subclasses `UsuarioComum` e `Administrador`; opção do administrador para ver os usuários cadastrados |

<details>
<summary><b>📋 Ver checklist detalhado</b></summary>

<br>

**Release 1.0**
- [x] Cadastro de usuários com email institucional e código de verificação
- [x] Cursos
- [x] Login
- [x] Solicitações (título, descrição, local e foto)

**Release 2.0**

*Navegação e organização*
- [x] Mural com o feed de solicitações ativas e encerradas (visitantes também veem)
- [x] Menu principal
- [x] Pesquisa por palavra e filtro por departamento (#TAG)
- [x] Solicitações como classes (`Solicitacao` e subclasses por natureza)

*Segurança*
- [x] Senhas salvas com hash (PBKDF2-SHA256) e mostradas como `*` ao digitar
- [x] Login com limite de 3 tentativas
- [x] Bloqueio de email já cadastrado e tratamento de erro no envio do email
- [x] Dados salvos em `dados.json`

*Privacidade e acompanhamento*
- [x] Anonimato
- [x] Status: Pendente, Em andamento, Concluída e Recusada
- [x] Histórico de mudanças de status
- [x] Administrador definido por email

*Comunidade (inovação)*
- [x] Enquete de prioridade: Alta, Média ou Baixa (1 voto por pessoa)
- [x] Ranking de prioridade das solicitações abertas
- [x] Comentários nas solicitações

**Release 2.1**
- [x] Classe-mãe `Usuario`, com as subclasses `UsuarioComum` e `Administrador` (arquivo `usuarios.py`, que substitui o `admin.py`)
- [x] Perfil mostra o tipo do usuário (Usuário comum ou Administrador)
- [x] Menu usa polimorfismo: cada tipo de usuário informa as próprias opções extras
- [x] Alterar status passou a ser um método do `Administrador`
- [x] Administrador pode ver todos os usuários cadastrados e o tipo de cada um
- [x] Dados da versão 2.0 continuam funcionando

</details>

---

## 📦 Requisitos e importações

- **Python 3.8 ou superior.**
- **Nenhuma biblioteca externa:** o projeto usa só a biblioteca padrão do Python, então **não é preciso rodar `pip install`**.
- **Internet:** necessária no cadastro, para enviar o código de verificação pelo Gmail.

---

## ▶️ Como rodar

**1. Clone o repositório**
```bash
git clone https://github.com/Astexz7/CIIU.git
```

**2. Entre na pasta do projeto**
```bash
cd CIIU
```

**3. (Opcional) Crie e ative um ambiente virtual**
```bash
python -m venv .venv
```
```bash
# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate
```

**4. Execute**
```bash
python main.py
```

> Rode sempre **de dentro da pasta do projeto**: o arquivo `dados.json` é criado e lido na pasta onde o terminal está.

### Menu

Ao abrir, o programa mostra o **mural** com as solicitações ativas e encerradas. Visitantes podem pesquisar, filtrar, ver o ranking e os detalhes; as ações marcadas pedem login ou cadastro na hora.

```
[1] Pesquisar
[2] Filtrar por departamento (#TAG)
[3] Nova solicitação                      (precisa de login)
[4] Votar em prioridade (Enquete)         (precisa de login)
[5] Fazer Login / Cadastro  ou  Sair da conta
[6] Comentar em uma solicitação           (precisa de login)
[7] Ranking de prioridade
[8] Ver detalhes de uma solicitação
[9] Alterar status de solicitação         (só administrador)
[10] Ver usuários cadastrados             (só administrador)
[0] Fechar sistema
```

### Administrador

Os administradores são definidos pelo email, na lista `ADMINS` do arquivo `usuarios.py`. Para adicionar mais de um, separe os emails com vírgula:

```python
ADMINS = {"festo.murilo@ufrpe.br", "outro.admin@ufrpe.br"}
```

No cadastro, o sistema cria um objeto `Administrador` para os emails dessa lista e um `UsuarioComum` para os demais. O administrador faz login normalmente, com senha, e vê as opções 9 e 10.

---

## 📚 Bibliotecas utilizadas

Todas fazem parte da biblioteca padrão do Python.

| Biblioteca | Onde | Por que usamos |
|---|---|---|
| `smtplib` | `cadastro.py` | Conectar ao servidor do Gmail (SMTP com SSL) e enviar o código de verificação |
| `email.message` | `cadastro.py` | Montar o email (remetente, destinatário, assunto e texto) |
| `secrets` | `cadastro.py` | Gerar o código de verificação. Diferente de `random`, é feito para segurança e não é previsível |
| `sys` | `seguranca.py` | Ler o teclado tecla por tecla e escrever os asteriscos da senha |
| `msvcrt` (Windows) / `termios` e `tty` (Linux e macOS) | `seguranca.py` | Ler uma tecla por vez, sem mostrar o que é digitado, para exibir `*` no lugar de cada caractere da senha |
| `getpass` | `seguranca.py` | Plano B: esconde a senha quando o programa não roda num terminal de verdade (ex.: console de algumas IDEs) |
| `hashlib` | `seguranca.py` | Gerar o hash da senha com PBKDF2-SHA256 (200 mil iterações), para nunca guardar a senha em texto puro |
| `hmac` | `seguranca.py` | Comparar hashes com `compare_digest`, uma comparação segura |
| `os` | `seguranca.py` | Gerar o "sal" aleatório (`os.urandom`): senhas iguais viram hashes diferentes |
| `json` | `dados.py` | Salvar e carregar usuários e solicitações num arquivo de texto legível |
| `pathlib` | `dados.py` | Trabalhar com o caminho do arquivo `dados.json` |
| `datetime` | `solicitacoes.py`, `usuarios.py`, `comunidade.py` | Registrar a data das solicitações, das mudanças de status e dos comentários |
| `os` e `subprocess` | `menu.py` | Limpar a tela do terminal antes de mostrar o mural (`cls` no Windows, `clear` no Linux/macOS) |

---

## 🧩 Organização dos módulos

```
CIIU/
├── main.py            # ponto de entrada: carrega os dados e abre o menu
├── menu.py            # mural, menu principal, pesquisa e filtro
├── cadastro.py        # cadastro, validação do email @ufrpe.br e envio do código
├── login.py           # autenticação (3 tentativas)
├── seguranca.py       # hash de senhas (PBKDF2-SHA256) e leitura da senha com asteriscos
├── cursos.py          # lista de cursos da UFRPE e escolha do curso
├── solicitacoes.py    # classe Solicitacao e subclasses; criar, listar e ver detalhes
├── comunidade.py      # enquete de prioridade, comentários e ranking
├── usuarios.py        # classes Usuario, UsuarioComum e Administrador
├── dados.py           # salvar e carregar dados em dados.json
├── .gitignore         # arquivos que não vão para o GitHub
└── README.md
```

Dependências entre os módulos:

```
main.py ──► dados.py, menu.py
menu.py
 ├── cadastro.py ──► cursos.py, seguranca.py, usuarios.py
 ├── login.py ─────► seguranca.py
 ├── solicitacoes.py
 ├── comunidade.py ► solicitacoes.py
 ├── usuarios.py ──► seguranca.py, solicitacoes.py
 └── dados.py
```

Cada módulo cuida de uma responsabilidade. O `main.py` só carrega os dados e abre o menu; o `menu.py` mostra o mural e chama a função certa. As funções que alteram dados devolvem `True` quando algo mudou, e então o menu salva.

### Orientação a objetos

O projeto tem **duas hierarquias de classes**:

```
        Solicitacao                          Usuario
   /         |          \                   /       \
Estrutural Eletronico  UsoGeral     UsuarioComum   Administrador
```

**Usuários** (`usuarios.py`):

- **Herança:** `UsuarioComum` e `Administrador` herdam de `Usuario` o email, a senha (hash), o curso, o perfil e a conferência da senha.
- **Polimorfismo:** o `Administrador` **sobrescreve** os métodos `eh_admin()` (devolve `True`) e `opcoes_extras()` (devolve as opções 9 e 10). O menu só pergunta ao objeto logado quais opções ele tem, sem testar o tipo.
- **Métodos só do administrador:** `alterar_status()` e `listar_usuarios()`.
- **Fábrica:** `criar_usuario()` decide se o objeto será `Administrador` ou `UsuarioComum` pelo email.

**Solicitações** (`solicitacoes.py`):

- **Herança:** `SolicitacaoEstrutural`, `SolicitacaoEletronico` e `SolicitacaoUsoGeral` herdam tudo de `Solicitacao` e só trocam a `natureza` e os exemplos.
- **Polimorfismo:** ao criar uma solicitação, cada classe mostra os próprios exemplos com o método de classe `exemplos()`.
- **Métodos:** cada objeto sabe calcular o resultado da enquete (`calcular_prioridade`), a pontuação do ranking (`pontuacao`) e o que mostrar no lugar do autor (`autor_visivel`).
- **Conversão para o arquivo:** `para_dict()` transforma o objeto em dicionário para salvar no JSON, e `de_dict()` faz o caminho contrário, criando a subclasse certa.

---

## 💾 Como os dados são guardados

Tudo fica em `dados.json`, criado automaticamente no primeiro cadastro:

```json
{
  "usuarios": {
    "aluno@ufrpe.br": {
      "tipo": "Usuário comum",
      "senha": "<sal>:<hash PBKDF2-SHA256>",
      "curso": {"curso": "BACHARELADO EM SISTEMAS DE INFORMAÇÃO", "tag": "#DEINFO"}
    }
  },
  "solicitacoes": [
    {
      "id": 1, "natureza": "Eletrônico", "titulo": "Ar quebrado", "descricao": "Não liga",
      "local": "Bloco B", "foto": null, "autor": "aluno@ufrpe.br", "anonimo": true,
      "status": "Em andamento", "data": "25/11/2026 10:00",
      "votos": {"Alta": 2, "Media": 1, "Baixa": 0},
      "votantes": ["aluno@ufrpe.br", "..."],
      "historico": [{"de": "Pendente", "para": "Em andamento", "por": "admin@ufrpe.br", "data": "..."}],
      "comentarios": [{"autor": "aluno@ufrpe.br", "texto": "...", "data": "..."}]
    }
  ]
}
```

O `dados.json` está no `.gitignore` e **não vai para o GitHub**, porque contém os dados dos usuários.

---

## ⚠️ Limitações conhecidas

- **Interface em terminal:** a versão web ainda será desenvolvida.
- **Foto:** é registrada pelo caminho do arquivo, sem upload real.
- **Senha de app do Gmail no código (`cadastro.py`):** num sistema em produção, ela deveria vir de uma variável de ambiente.
- **Persistência em JSON:** suficiente para o protótipo; um banco de dados é o próximo passo.
- **Filtro por departamento:** usa a tag do curso de quem relatou, e não o departamento do local do problema.

---

## 👥 Equipe

| 👤 Nome |
|---|
| **Lucas Manoel de Holanda** |
| **Festo Murilo** |
| **Nicolas Rodrigues** |

---

<div align="center">

🏛️ **CIIU** · Feito por alunos, para alunos

</div>
