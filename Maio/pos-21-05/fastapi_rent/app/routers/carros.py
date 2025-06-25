from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Carro
from app.database import carros

router = APIRouter(prefix="/carros", tags=["Carros"])

@router.get("/", response_model=List[Carro])
def listar_carros():
    return carros

@router.post("/", response_model=Carro)
def adicionar_carro(carro: Carro):
    for c in carros:
        if c.id == carro.id:
            raise HTTPException(status_code=400, detail="ID de carro já existe.")
    carros.append(carro)
    return carro

@router.put("/{id}", response_model=Carro)
def atualizar_carro(id: int, carro: Carro):
    for i, c in enumerate(carros):
        if c.id == id:
            carros[i] = carro
            return carro
    raise HTTPException(status_code=404, detail="Carro não encontrado.")

@router.delete("/{id}")
def remover_carro(id: int):
    for i, c in enumerate(carros):
        if c.id == id:
            carros.pop(i)
            return {"mensagem": "Carro removido com sucesso."}
    raise HTTPException(status_code=404, detail="Carro não encontrado.")

@router.get("/disponiveis", response_model=List[Carro])
def listar_carros_disponiveis():
    return [c for c in carros if c.disponivel]
