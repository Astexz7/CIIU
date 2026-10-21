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
| **1.1** | Privacidade e acompanhamento | Registro anônimo e status da solicitação |
| **1.2** | Comunidade | Comentários e enquete de importância |

<details>
<summary><b>📋 Ver checklist detalhado</b></summary>

<br>

**Release 1.0**
- [ ] Cadastro de usuários
- [ ] Cursos
- [ ] Login
- [ ] Solicitações (título, descrição, local e foto)

**Release 1.1**
- [ ] Opção de registro anônimo
- [ ] Status da solicitação (pendente / em andamento / concluída)

**Release 1.2**
- [ ] Comentários nas solicitações
- [ ] Enquete de importância

</details>

---

## 🧰 Tecnologias

O projeto está sendo desenvolvido em **Python**.

---

## 📁 Estrutura do projeto

```
CIIU/
├── main.py            # ponto de entrada
├── cadastro.py
├── cursos.py
├── login.py
├── solicitacoes.py
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
