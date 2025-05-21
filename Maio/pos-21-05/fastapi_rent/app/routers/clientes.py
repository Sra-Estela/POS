from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Cliente
from app.database import clientes

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get("/", response_model=List[Cliente])
def listar_clientes():
    return clientes

@router.post("/", response_model=Cliente)
def adicionar_cliente(cliente: Cliente):
    for c in clientes:
        if c.id == cliente.id:
            raise HTTPException(status_code=400, detail="ID de cliente já existe.")
    clientes.append(cliente)
    return cliente

@router.get("/{id}", response_model=Cliente)
def buscar_cliente(id: int):
    for c in clientes:
        if c.id == id:
            return c
    raise HTTPException(status_code=404, detail="Cliente não encontrado.")
