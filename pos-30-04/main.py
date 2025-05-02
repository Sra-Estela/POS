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
