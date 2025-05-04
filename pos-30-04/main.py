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