<div align="center">

# 🏛️ CIIU

### Centro de Informação de Infraestrutura Universitária

*Um canal único para o aluno reportar problemas de infraestrutura no campus e acompanhar até quando eles são resolvidos.*

[Sobre](#-sobre-o-projeto) •
[Como funciona](#-como-funciona) •
[Releases](#-releases) •
[Tecnologias](#-tecnologias) •
[Estrutura](#-estrutura-do-projeto) •
[Como rodar](#-como-rodar) •
[Equipe](#-equipe)

</div>

---

## 💡 Sobre o projeto

Ar-condicionado quebrado, banheiro sem manutenção, bebedouro parado, lâmpada queimada. Quase todo aluno já viu um problema desses, mas poucos sabem a quem avisar, e quem avisa raramente descobre se alguma coisa foi feita.

O CIIU reúne essas reclamações e sugestões em um só lugar, com **participação dos alunos** e **transparência no andamento** de cada solicitação.

---

## ✨ Como funciona

| Passo | O que acontece |
|:---:|---|
| **1** | 👤 O aluno cria uma conta com e-mail, senha e curso |
| **2** | 📝 Registra um problema com título, descrição, local e foto |
| **3** | 🕶️ Pode marcar o registro como anônimo, e o nome fica oculto para o público |
| **4** | 💬 A comunidade comenta e participa da enquete de importância |
| **5** | 📊 A solicitação avança pelos status abaixo |

```
🟡 Pendente   ➜   🔵 Em andamento   ➜   🟢 Concluída
```

> 🔒 **Sobre o anonimato:** ele é apenas de exibição. O autor continua salvo no banco de dados, mas não aparece publicamente quando o problema é anônimo.

---

## 🚀 Releases

| Release | Foco | Entregas |
|:---:|---|---|
| **1.0** | Base do sistema | Cadastro de usuários, cursos, login e solicitações |
| **2.0** | Segurança, persistência e administração | Menu principal, senhas com hash, dados salvos em arquivo, solicitações completas com anonimato, enquentes de prioridade, status de solicitações e painel do administrador |

<details>
<summary><b>📋 Ver checklist detalhado</b></summary>

<br>

**Release 1.0**
- [x] Cadastro de usuários
- [x] Cursos
- [x] Login
- [x] Solicitações (título, descrição, local e foto)

**Release 2.0**

*Navegação*
- [x] Menu principal (cadastrar, login, nova solicitação, ver solicitações, sair da conta)
- [x] Nova solicitação só pode ser criada por quem está logado

*Segurança*
- [x] Senhas salvas com hash (PBKDF2-SHA256), nunca em texto puro
- [x] Senha escondida enquanto é digitada
- [x] Login com limite de 3 tentativas
- [x] Código de verificação gerado com `secrets`
- [x] Validação de email institucional mais rígida e bloqueio de email já cadastrado
- [x] Tratamento de erro no envio do email (o programa não fecha mais)

*Solicitações*
- [x] Título, descrição, local, foto (opcional) e data
- [x] Opção de anonimato (o autor continua salvo, mas aparece como "Anônimo")
- [x] Status inicial "Pendente"
- [x] Campos obrigatórios não aceitam texto vazio

*Persistência*
- [x] Usuários e solicitações salvos em `dados.json` e carregados ao abrir o programa

*Administrador*
- [x] Administradores definidos por email
- [x] Alterar status: Pendente → Em andamento → Concluída
- [x] Histórico de mudanças de status visível para todos
- [x] Administrador vê o autor real das solicitações anônimas

*Organização*
- [x] `.gitignore` e remoção do `__pycache__` do repositório
- [x] Código comentado linha a linha

</details>

---

## 🧰 Tecnologias

O projeto está sendo desenvolvido em **Python**.

---

## 📁 Estrutura do projeto

```
CIIU/
├── main.py            # ponto de entrada
├── cadastro.py        # cadastro e verificação de email
├── cursos.py          # lista de cursos da UFRPE
├── login.py
├── solicitacoes.py    # registrar e listar solicitações
├── seguranca.py       # hash e conferência de senhas
├── dados.py           # salva e carrega dados em dados.json
├── admin.py           # funções do administrador (alterar status)
└── README.md
```

> A estrutura pode mudar conforme o projeto evolui.

---

## ▶️ Como rodar

**Pré-requisito:** Python 3 instalado.

**1. Clone o repositório**
```bash
git clone https://github.com/Astexz7/CIIU.git
```

**2. Acesse a pasta do projeto**
```bash
cd CIIU
```

**3. Crie um ambiente virtual**
```bash
python -m venv .venv
```

**4. Ative o ambiente virtual**

```bash
# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate
```

**5. Execute o projeto**
```bash
python main.py
```

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
