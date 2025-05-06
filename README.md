## Atividade de `Ajax` e `JQuery` dia 3 de abril de 2025.
### Esquema de rotas:
```
|pos-30-04/
│  ├──__pycache__/
│  ├──.virtual/
│  ├──static/css/
|  │  ├──cadastrar_tarefa.css
|  │  └──listar_tarefas.css
│  ├──templates/
|  │  ├──cadastrar_tarefa.html
|  │  └──listar_tarefas.html
├──models.py
├──main.py
└──requeriments.txt
```
---

### Arquivo `static/css/cadastrar_tarefa.css`:
```css
/* Reset básico */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Container principal */
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

### Arquivo `static/css/listar_tarefas.css`:
```css
/* Reset básico */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Container principal */
.container {
    max-width: 800px; /* Aumentei a largura para acomodar a tabela */
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

/* Estilos da tabela */
table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}

th, td {
    padding: 12px 15px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}

th {
    background-color: #f2f2f2;
    font-weight: bold;
}

tbody tr:nth-child(even) {
    background-color: #f9f9f9;
}

/* Botão de Excluir */
.excluir-btn {
    background-color: #f44336;
    color: white;
    padding: 8px 12px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.excluir-btn:hover {
    background-color: #da190b;
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
    <link rel="stylesheet" href="/static/css/cadastrar_tarefa.css">
</head>
<body>
    <div class="container">
        <div class="menu">
            <a href="/"><button>Cadastrar</button></a>
            <a href="/tarefas/"><button>Listar</button></a>
        </div>
        <div class="conteudo">
            <div class="cadastrar">
                <h1>CADASTRO DE TAREFA</h1>
                <form id="formTarefa">
                    <label for="titulo">Título da Tarefa:</label><br>
                    <input type="text" id="titulo" name="titulo" placeholder="Dê um título à sua Tarefa" required><br><br>

                    <label for="descricao">Descrição da Tarefa:</label><br>
                    <input type="text" id="descricao" name="descricao" required><br><br>

                    <label for="concluido">Concluído:</label><br>
                    <select id="concluido" name="concluido" required>
                        <option value="true">Sim</option>
                        <option value="false">Não</option>
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
            let nextId = 1; // Inicializa o ID

            $("#formTarefa").on("submit", function(e) {
                e.preventDefault(); // evita recarregar a página

                // Incrementa o ID ANTES da requisição
                const currentId = nextId++;

                // Dados do formulário
                const tarefa = {
                    id: currentId, // Usa o ID atual
                    titulo: $("#titulo").val(),
                    descricao: $("#descricao").val(),
                    concluido: $("#concluido").val() === "true"  // Converte para booleano
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
                        // Se a requisição falhar, decrementa o nextId para evitar lacunas
                        nextId--;
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
    <link rel="stylesheet" href="/static/css/listar_tarefas.css">
</head>
<body>
    <div class="container">
        <div class="menu">
            <a href="/"><button>Cadastrar</button></a>
            <a href="/tarefas/"><button>Listar</button></a>
        </div>
        <h1>Listagem de Tarefas</h1>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Título</th>
                    <th>Descrição</th>
                    <th>Concluído</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody>
                {% for tarefa in tarefas %}
                <tr>
                    <td>{{ tarefa.id }}</td>
                    <td>{{ tarefa.titulo }}</td>
                    <td>{{ tarefa.descricao }}</td>
                    <td>{{ tarefa.concluido }}</td>
                    <td>
                        <button class="excluir-btn" data-tarefa-id="{{ tarefa.id }}">Excluir</button>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>

    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        $(document).ready(function() {
            $(".excluir-btn").click(function() {
                const tarefaId = $(this).data("tarefa-id");
                excluirTarefa(tarefaId);
            });

            function excluirTarefa(tarefaId) {
                $.ajax({
                    url: "http://localhost:8000/tarefas/" + tarefaId,
                    type: "DELETE",
                    success: function(response) {
                        // Recarrega a página para atualizar a lista
                        window.location.reload();
                    },
                    error: function(xhr, status, error) {
                        console.error("Erro ao excluir tarefa:", xhr.responseText);
                        alert("Erro ao excluir tarefa.");
                    }
                });
            }
        });
    </script>
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
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuração do Jinja2 para buscar os templates na pasta 'templates'
templates = Jinja2Templates(directory="templates")

# Definir a pasta estática para arquivos como CSS e JS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar o middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000"],  # Permite o frontend
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todos os headers
)

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
    return tarefa # Retorna apenas o objeto Tarefa
    #return {"message": "Tarefa criada com sucesso!", "tarefa": tarefa} # Antes

@app.delete("/tarefas/{tarefa_id}")
async def excluir_tarefa(tarefa_id: int):
    global tarefas
    tarefas = [tarefa for tarefa in tarefas if tarefa.id != tarefa_id]
    return {"message": "Tarefa excluída com sucesso!"}
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
certifi==2025.4.26
click==8.1.8
colorama==0.4.6
dnspython==2.7.0
email_validator==2.2.0
fastapi==0.115.12
fastapi-cli==0.0.7
h11==0.16.0
httpcore==1.0.9
httptools==0.6.4
httpx==0.28.1
idna==3.10
Jinja2==3.1.6
markdown-it-py==3.0.0
MarkupSafe==3.0.2
mdurl==0.1.2
pydantic==2.11.4
pydantic_core==2.33.2
Pygments==2.19.1
python-dotenv==1.1.0
python-multipart==0.0.20
PyYAML==6.0.2
rich==14.0.0
rich-toolkit==0.14.4
shellingham==1.5.4
sniffio==1.3.1
starlette==0.46.2
typer==0.15.3
typing-inspection==0.4.0
typing_extensions==4.13.2
uvicorn==0.34.2
watchfiles==1.0.5
websockets==15.0.1

```

---