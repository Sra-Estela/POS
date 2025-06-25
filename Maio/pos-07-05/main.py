from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from models import Usuario, Livro, Biblioteca, Emprestimo
from fastapi.templating import Jinja2Templates
from typing import List
from datetime import datetime

app = FastAPI()

templates = Jinja2Templates(directory="templates")

usuarios: List[Usuario] = []
livros: List[Livro] = []
bibliotecas: List[Biblioteca] = []
emprestimos: List[Emprestimo] = []

# Rota para exibir o HTML
@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- USUÁRIO -=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-

@app.get("/usuarios")
def listar_usuarios():
    return usuarios

@app.post("/usuarios")
def adicionar_usuario(usuario: Usuario):
    usuarios.append(usuario)
    return {"mensagem": "Usuário adicionado com sucesso."}

@app.delete("/usuarios/{username}")
def deletar_usuario(username: str):
    for u in usuarios:
        if u.username == username:
            usuarios.remove(u)
            return {"mensagem": "Usuário removido com sucesso."}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- LIVRO -=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-

@app.get("/livros", response_model=List[Livro])
def listar_livros():
    return livros

@app.post("/livros")
def adicionar_livro(livro: Livro):
    livros.append(livro)
    return {"mensagem": "Livro removido com sucesso."}

@app.delete("/livros/{titulo}")
def deletar_livro(titulo: str):
    for l in livros:
        if l.titulo == titulo:
            livros.remove(l)
            return {"mensagem": "Livro removido com sucesso."}
    raise HTTPException(status_code=404, detail="Livro não encontrado")

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- BIBLIOTECA -=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-

@app.get("/bibliotecas", response_model=List[Biblioteca])
def listar_biblioteca():
    return bibliotecas

@app.post("/bibliotecas")
def adicionar_biblioteca(biblioteca: Biblioteca):
    bibliotecas.append(biblioteca)
    return {"mensagem": "Biblioteca adicionada com sucesso."}

@app.delete("/bibliotecas/{nome}")
def deletar_biblioteca(nome: str):
    for b in bibliotecas:
        if b.nome == nome:
            bibliotecas.remove(b)
            return {"mensagem": "Biblioteca removida com sucesso."}
    raise HTTPException(status_code=404, detail="Biblioteca não encontrada")

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- EMPRÉSTIMO -=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-

@app.get("/emprestimos", response_model=List[Emprestimo])
def listar_emprestimos():
    return emprestimos

@app.post("/emprestimos")
def adicionar_emprestimo(emprestimo: Emprestimo):
    emprestimos.append(emprestimo)
    return {"mensagem": "Empréstimo registrado com sucesso."}

@app.delete("/emprestimos")
def deletar_emprestimo(usuario: str, livro: str):
    for e in emprestimos:
        if e.usuario.username == usuario and e.livro.titulo == livro:
            emprestimos.remove(e)
            return {"mensagem": "Empréstimo removido com sucesso."}
    raise HTTPException(status_code=404, detail="Empréstimo não encontrado")