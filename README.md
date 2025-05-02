## Atividade de `Ajax` e `JQuery` dia 3 de abril de 2025.
### Esquema de rotas:
```
|pos-30-04/
│  ├──__pycache__/
│  ├──.virtual/
│  ├──static/css/
|  │  └──style.css
│  ├──templates/
|  │  ├──cadastrar_tarefa.html
|  │  └──listar_tarefas.html
├──models.py
├──main.py
└──requeriments.txt
```
---

### Arquivo `static/css/style.css`:
```css
/* Reset básico */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Container principal */
/* .container {
    max-width: 600px;
    margin: 50px auto;
    padding: 30px;
    background-color: #fefefe;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
} */

.conteudo {
    max-width: 600px;
    margin: 50px auto;
    padding: 30px;
    background-color: #fefefe;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

/* Cabeçalho */
h1 {
    text-align: center;
    color: #333;
    margin-bottom: 20px;
}

/* Botões do menu */
.menu {
    display: flex;
    justify-content: center;
    gap: 20px;
    padding: 10px;
    background-color: whitesmoke;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2) 
}

.menu button {
    background-color: #4CAF50;
    color: white;
    padding: 10px 18px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 15px;
    transition: background-color 0.3s;
}

.menu button:hover {
    background-color: #45a049;
}

/* Campos do formulário */
form label {
    font-weight: bold;
    color: #444;
}

form input[type="text"],
form input[type="datetime-local"],
form select {
    width: 100%;
    padding: 10px;
    margin-top: 6px;
    margin-bottom: 16px;
    border: 1px solid #ccc;
    border-radius: 6px;
}

form input[type="submit"] {
    width: 100%;
    background-color: #2196F3;
    color: white;
    padding: 12px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.3s;
}

form input[type="submit"]:hover {
    background-color: #1976D2;
}

/* Mensagem de feedback */
#mensagem {
    margin-top: 15px;
    text-align: center;
    font-weight: bold;
    color: #2e7d32;
}

```

---

### Arquivo `templates/cadastrar_tarefa.html`:
```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Cadastro de Tarefa</title>
    <link rel="stylesheet" href="../static/css/style.css">
</head>
<body>
    <div class="container">
        <div class="menu">
            <a href="cadastrar_tarefa.html"><button>Cadastrar</button></a>
            <a href="listar_tarefas.html"><button>Listar</button></a>
        </div>
        <div class="conteudo">
            <div class="cadastrar">
                <h1>CADASTRO DE TAREFA</h1>
                <form id="formTarefa">
                    <label for="nome_tarefa">Nome da Tarefa:</label><br>
                    <input type="text" id="nome_tarefa" placeholder="Dê nome à sua Tarefa" required><br><br>

                    <label for="data_entrega">Data de Entrega:</label><br>
                    <input type="datetime-local" id="data_entrega" required><br><br>

                    <label for="disciplinas">Selecione a disciplina:</label><br>
                    <select id="disciplinas" required>
                        <option value="Português">Português</option>
                        <option value="P.O.S.">P.O.S.</option>
                        <option value="História">História</option>
                        <option value="Biologia">Biologia</option>
                        <option value="P.I.U">P.I.U</option>
                    </select><br><br>

                    <input type="submit" value="Criar">
                </form>
                <p id="mensagem"></p>
            </div>
        </div>
    </div>

    <!-- jQuery CDN -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

    <!-- Script para enviar tarefa -->
    <script>
        $(document).ready(function() {
            $("#formTarefa").on("submit", function(e) {
                e.preventDefault(); // evita recarregar a página

                // Dados do formulário
                const tarefa = {
                    nome: $("#nome_tarefa").val(),
                    data_entrega: $("#data_entrega").val(),
                    disciplina: $("#disciplinas").val()
                };

                // Envia para a API
                $.ajax({
                    url: "http://localhost:8000/tarefas/",
                    type: "POST",
                    contentType: "application/json",
                    data: JSON.stringify(tarefa),
                    success: function(response) {
                        $("#mensagem").text("Tarefa cadastrada com sucesso!");
                        $("#formTarefa")[0].reset(); // limpa o formulário
                    },
                    error: function(xhr, status, error) {
                        $("#mensagem").text("Erro ao cadastrar tarefa.");
                        console.error(xhr.responseText);
                    }
                });
            });
        });
    </script>
</body>
</html>

```

---

### Arquivo `templates/listar_tarefas.html`:
```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Listagem de Tarefas</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <div class="container">
        <h1>Listagem de Tarefas</h1>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>Data de Entrega</th>
                    <th>Disciplina</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody>
                {% for tarefa in tarefas %}
                <tr>
                    <td>{{ tarefa.id }}</td>
                    <td>{{ tarefa.nome_tarefa }}</td>
                    <td>{{ tarefa.data_entrega }}</td>
                    <td>{{ tarefa.disciplinas }}</td>
                    <td>
                        <form action="/tarefas/{{ tarefa.id }}" method="post">
                            <input type="submit" value="Excluir">
                        </form>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</body>
</html>

```

---

### Arquivo `main.py`:
```python
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from models import Tarefa
from typing import List
from fastapi import Request

app = FastAPI()

# Configuração do Jinja2 para buscar os templates na pasta 'templates'
templates = Jinja2Templates(directory="templates")

# Definir a pasta estática para arquivos como CSS e JS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Lista de tarefas (simulando um banco de dados)
tarefas: List[Tarefa] = []

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # Renderiza o HTML de cadastro de tarefa
    return templates.TemplateResponse("cadastrar_tarefa.html", {"request": request})

@app.get("/tarefas/", response_class=HTMLResponse)
async def listar_tarefas(request: Request):
    # Renderiza a página de listagem de tarefas, passando a lista de tarefas para o template
    return templates.TemplateResponse("listar_tarefas.html", {"request": request, "tarefas": tarefas})

@app.post("/tarefas/", response_model=Tarefa)
async def criar_tarefa(tarefa: Tarefa):
    # Adiciona a nova tarefa na lista
    tarefa.id = len(tarefas) + 1
    tarefas.append(tarefa)
    # Após a criação, redireciona para a página de listagem de tarefas
    return {"message": "Tarefa criada com sucesso!", "tarefa": tarefa}

@app.delete("/tarefas/{tarefa_id}", response_model=Tarefa)
async def excluir_tarefa(tarefa_id: int):
    # Tenta localizar a tarefa pelo ID e a exclui
    for index, tarefa in enumerate(tarefas):
        if tarefa_id == tarefa.id:
            del tarefas[index]
            return tarefa
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

```

---

### Arquivo `models.py`:
```python
from pydantic import BaseModel

class Tarefa(BaseModel):
    id: int
    titulo: str
    descricao: str
    concluido: bool
```

---

### Arquivo `requirements.txt`:
```txt
annotated-types==0.7.0
anyio==4.9.0
click==8.1.8
colorama==0.4.6
fastapi==0.115.12
h11==0.16.0
idna==3.10
Jinja2==3.1.6
MarkupSafe==3.0.2
pydantic==2.11.4
pydantic_core==2.33.2
sniffio==1.3.1
starlette==0.46.2
typing-inspection==0.4.0
typing_extensions==4.13.2
uvicorn==0.34.2

```

---