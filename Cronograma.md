# 🧠 Cronograma de Estudos – Programação Orientada a Serviços

## 📅 Estrutura semanal
- **Seg a Sex:** Teoria + prática (1h30/dia)
- **Sábado (opcional):** Revisão e prática extra
- **Domingo:** Descanso ou revisão leve

---

## ✅ Semana 1 – Estrutura e Descrição de Dados

### 📘 Conteúdo
- Linguagens de descrição de dados
- XML, JSON, YAML
- DTD e XML Schema
- DOM

### 🔗 Materiais
- [W3Schools - XML](https://www.w3schools.com/xml/)
- [JSON - MDN](https://developer.mozilla.org/pt-BR/docs/Learn/JavaScript/Objects/JSON)
- [YAML - yaml.org](https://yaml.org/)
- [DOM - MDN](https://developer.mozilla.org/pt-BR/docs/Web/API/Document_Object_Model)
- [Vídeo: XML vs JSON vs YAML](https://www.youtube.com/watch?v=UMGgXvU5WFk)

### ✅ Prática
- Criar arquivos XML, JSON e YAML com os mesmos dados.
- Criar XML com DTD e converter para XML Schema.
- Simular formulário HTML que gera JSON via JS.

---

## ✅ Semana 2 – HTML, CSS e Frontend com jQuery/Ajax

### 📘 Conteúdo
- HTML/CSS básico
- Interface única com modal (tela única)
- jQuery + Ajax para comunicação com API

### 🔗 Materiais
- [W3Schools - HTML e CSS](https://www.w3schools.com/html/)
- [jQuery AJAX API](https://api.jquery.com/jQuery.ajax/)
- [Vídeo: jQuery + AJAX](https://www.youtube.com/watch?v=9Z9xKWfEn_4)

### ✅ Prática
- Criar `listarTarefa.html` com tabela e botão de excluir.
- Criar botão de "Cadastrar" que abre um modal.
- Enviar os dados com `$.ajax()`.

---

## ✅ Semana 3 – FastAPI + CRUD: Biblioteca e Veículos

### 📘 Conteúdo
- Introdução à FastAPI
- Pydantic para validação
- CRUD básico com dados em memória

### 🔗 Materiais
- [FastAPI (pt)](https://fastapi.tiangolo.com/pt/)
- [Vídeo: FastAPI do Zero](https://www.youtube.com/watch?v=KDN3JJcgnpY)

### ✅ Prática
- Criar API com entidades de **biblioteca**.
- Criar API de **veículos** com CRUD completo.
- Testar com FastAPI Docs UI.

---

## ✅ Semana 4 – Consumo de API com Python Terminal

### 📘 Conteúdo
- Consumo de API com `requests`
- Menu interativo no terminal
- Edição e exclusão com base em busca

### 🔗 Materiais
- [Requests Docs](https://docs.python-requests.org/en/latest/)
- [Tutorial: Requests](https://realpython.com/python-requests/)

### ✅ Prática
- Criar menu com:
  - Listar
  - Pesquisar por título
  - Cadastrar livro
  - Deletar livro
  - Editar livro
- Validar erros (livro inexistente, dados inválidos)

---

## ✅ Semana 5 – Sistema de Reservas + FastAPI Avançado

### 📘 Conteúdo
- Relacionamentos entre entidades
- Filtros, parâmetros e status code
- Erros customizados

### 🔗 Materiais
- [Pydantic Nested Models](https://docs.pydantic.dev/latest/usage/models/#recursive-models)
- [Tratamento de erros – FastAPI](https://fastapi.tiangolo.com/tutorial/handling-errors/)

### ✅ Prática
- Criar sistema de reservas:
  - Carro, Cliente, Reserva
  - Validar datas e disponibilidade
- Endpoints:
  - `GET`, `POST`, `PUT`, `DELETE`
  - `/carros/disponiveis`, `/clientes/{id}`, etc.

---

## ✅ Semana 6 – Containers e Orquestração

### 📘 Conteúdo
- Docker, Podman, Containerd
- Kubernetes básico
- Rancher Desktop

### 🔗 Materiais
- [Curso Docker para Iniciantes](https://www.youtube.com/watch?v=DnT3LRZ54Hk)
- [Podman vs Docker](https://www.redhat.com/sysadmin/podman-docker-cheat-sheet)
- [Kubernetes Docs PT-BR](https://kubernetes.io/pt/docs/home/)
- [Rancher Desktop](https://rancherdesktop.io/)

### ✅ Prática
- Dockerizar API da semana 5
- Executar container localmente
- Usar Rancher Desktop ou Minikube (opcional)

---

## 📚 Extras e Apoio

### Plataformas de Estudo e Prática
- [Beecrowd](https://www.beecrowd.com.br/)
- [DevMedia](https://www.devmedia.com.br/)
- [Exercism](https://exercism.org/)
- [Postman](https://www.postman.com/)

---

### ✨ Dica Final
> Sempre teste os endpoints criados com o Swagger da FastAPI ou com Postman. Anote erros comuns que aparecem no terminal, pois esses são cobrados nas provas!

Claro! Aqui vai uma seleção de **materiais organizados por tópicos** que vão te ajudar a dominar tudo o que essa atividade envolve — desde leitura de CSV até criação de APIs e consumo em terminal.

---

## 📚 Materiais para Estudo – Atividade de Consulta por ID com FastAPI

---

### 🔢 1. **Leitura e manipulação de CSV com pandas**

| Tópico                                    | Material                                                                                       |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------- |
| 📖 Documentação pandas – `read_csv()`     | [pandas.read\_csv() – Docs](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) |
| 🎥 Vídeo: Introdução ao pandas (com CSVs) | [Curso em Vídeo – pandas](https://www.youtube.com/watch?v=KzD9A1VRE7g)                         |
| 🧪 Exercício: Filtrar linha por ID        | `python\ndf[df['IdPedido'] == 123456]\n`                                                       |

---

### 🚀 2. **FastAPI – Criação de API REST**

| Tópico                                    | Material                                                                      |
| ----------------------------------------- | ----------------------------------------------------------------------------- |
| 📖 Documentação oficial                   | [FastAPI Docs (PT-BR)](https://fastapi.tiangolo.com/pt/)                      |
| 🎥 Vídeo: FastAPI do zero ao deploy       | [FastAPI + Python - CFBCursos](https://www.youtube.com/watch?v=KDN3JJcgnpY)   |
| 📘 Artigo: Como criar uma API com FastAPI | [Dev.to - FastAPI](https://dev.to/tiangolo/fastapi-python-api-framework-1dj5) |
| 🔧 Exemplo prático                        | `python\n@app.get("/pedido/{id}")\ndef get_pedido(id: int):\n    ...\n`       |

---

### 🌐 3. **Tratamento de Erros com HTTPException**

| Tópico                      | Material                                                                            |
| --------------------------- | ----------------------------------------------------------------------------------- |
| 📘 HTTPException no FastAPI | [Handling Errors – FastAPI](https://fastapi.tiangolo.com/tutorial/handling-errors/) |
| 🧪 Exemplo:                 | `python\nraise HTTPException(status_code=404, detail=\"Pedido não encontrado\")\n`  |

---

### 📦 4. **Consumo de API com `requests` (Terminal)**

| Tópico                           | Material                                                                     |
| -------------------------------- | ---------------------------------------------------------------------------- |
| 📖 Docs oficial do `requests`    | [requests.readthedocs.io](https://requests.readthedocs.io/en/latest/)        |
| 🎥 Vídeo: Requisições com Python | [Requests com Python - Hashtag](https://www.youtube.com/watch?v=qbW6FRbaSl0) |
| 🧪 Exemplo prático:              | `python\nrequests.get(\"http://127.0.0.1:8000/pedido/123\")\n`               |

---

### 🧠 5. **Extras úteis**

| Tema                                          | Link                                                                                                                |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| 🧪 Ferramenta para testar APIs                | [Postman](https://www.postman.com/)                                                                                 |
| 📄 Conversor CSV → JSON Online (visualização) | [ConvertCSV.com](https://www.convertcsv.com/csv-to-json.htm)                                                        |
| 👩🏽‍💻 Curso gratuito de Python + APIs       | [Python e APIs REST - Curso do Guanabara](https://www.youtube.com/playlist?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6) |

---

Se quiser, posso montar um **PDF ou página estilo guia de estudos** com tudo isso organizado por módulos. Deseja esse formato também?

Claro, Estela! Aqui está uma **atividade prática autoral**, bem parecida com a original, cobrindo os mesmos objetivos — manipulação de CSV, criação de API REST com FastAPI, leitura por ID e consumo via terminal.

---

## 🧪 **Atividade Prática para Treino – Cadastro de Alunos**

### 📁 Estrutura do arquivo CSV: `alunos.csv`

O arquivo contém registros de alunos matriculados em um sistema educacional.

| Campo             | Tipo       | Descrição                                                     |
| ----------------- | ---------- | ------------------------------------------------------------- |
| `IdAluno`         | inteiro    | Identificador único do aluno (chave primária)                 |
| `Nome`            | texto(100) | Nome completo do aluno                                        |
| `Idade`           | inteiro    | Idade do aluno                                                |
| `Curso`           | texto(100) | Nome do curso que o aluno está matriculado                    |
| `Campus`          | texto(50)  | Nome do campus                                                |
| `DataMatricula`   | data       | Data de matrícula no curso (formato DD/MM/AAAA)               |
| `StatusMatricula` | texto(20)  | Situação atual: "Ativo", "Trancado", "Cancelado", "Concluído" |

---

## 🎯 **Objetivo da atividade**

* Criar uma API com FastAPI que permita:

  * Buscar os dados de um aluno por `IdAluno`
  * Retornar os dados em formato JSON
  * Retornar erro 404 caso o ID não exista

* Criar uma aplicação de terminal que:

  * Peça ao usuário o `IdAluno`
  * Consulte a API e imprima os dados, ou informe se não foi encontrado

---

## 🧰 **O que você deve fazer**

### 📄 1. Criar o arquivo `alunos.csv` com pelo menos 10 alunos fictícios.

Exemplo:

```csv
IdAluno;Nome;Idade;Curso;Campus;DataMatricula;StatusMatricula
1001;João da Silva;20;Engenharia de Computação;Caicó;01/02/2023;Ativo
1002;Maria Oliveira;22;Direito;Natal;10/03/2022;Trancado
1003;Lucas Andrade;19;Administração;Caicó;15/01/2024;Ativo
...
```

---

### 🧑‍💻 2. Criar o backend (API FastAPI)

#### Requisitos:

* `GET /aluno/{id}`
* Ler o `alunos.csv` (use `pandas.read_csv(..., encoding='utf-8', sep=';')`)
* Retornar os dados ou erro 404 com `"Aluno não encontrado"`.

---

### 🖥️ 3. Criar o terminal de consulta

#### Requisitos:

* Pedir `IdAluno` via `input()`
* Usar `requests.get()` para buscar na API
* Imprimir os dados ou mensagem de erro

---

## ✅ Critérios avaliados

| Critério                    | Obrigatório |
| --------------------------- | ----------- |
| Leitura correta do CSV      | ✅           |
| Busca por ID                | ✅           |
| Tratamento de erro (404)    | ✅           |
| Consumo da API via terminal | ✅           |
| Estrutura clara do JSON     | ✅           |

---

Se quiser, posso montar:

* O CSV de exemplo
* A API pronta
* O terminal consumidor

Você quer isso agora?
