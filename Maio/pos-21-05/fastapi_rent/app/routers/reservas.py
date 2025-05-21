from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Reserva
from app.database import reservas, carros, clientes

router = APIRouter(prefix="/reservas", tags=["Reservas"])

@router.post("/", response_model=Reserva)
def criar_reserva(reserva: Reserva):
    cliente = next((c for c in clientes if c.id == reserva.cliente_id), None)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")

    carro = next((c for c in carros if c.id == reserva.carro_id), None)
    if not carro:
        raise HTTPException(status_code=404, detail="Carro não encontrado.")

    if not carro.disponivel:
        raise HTTPException(status_code=400, detail="Carro indisponível para reserva.")

    if reserva.data_fim < reserva.data_inicio:
        raise HTTPException(status_code=400, detail="Data de fim não pode ser anterior à data de início.")

    reservas.append(reserva)
    carro.disponivel = False
    return reserva

@router.get("/", response_model=List[Reserva])
def listar_reservas():
    return reservas

@router.delete("/{id}")
def cancelar_reserva(id: int):
    for i, r in enumerate(reservas):
        if r.id == id:
            carro = next((c for c in carros if c.id == r.carro_id), None)
            if carro:
                carro.disponivel = True
            reservas.pop(i)
            return {"mensagem": "Reserva cancelada com sucesso."}
    raise HTTPException(status_code=404, detail="Reserva não encontrada.")
