from app.database import reservas, carros, clientes
from app.models import Reserva

def criar_reserva(reserva: Reserva):
    cliente = next((c for c in clientes if c.id == reserva.cliente_id), None)
    if not cliente:
        raise LookupError("Cliente não encontrado.")

    carro = next((c for c in carros if c.id == reserva.carro_id), None)
    if not carro:
        raise LookupError("Carro não encontrado.")

    if not carro.disponivel:
        raise ValueError("Carro indisponível para reserva.")

    if reserva.data_fim < reserva.data_inicio:
        raise ValueError("Data de fim não pode ser anterior à data de início.")

    reservas.append(reserva)
    carro.disponivel = False
    return reserva

def listar_reservas():
    return reservas

def cancelar_reserva(id: int):
    for i, r in enumerate(reservas):
        if r.id == id:
            carro = next((c for c in carros if c.id == r.carro_id), None)
            if carro:
                carro.disponivel = True
            reservas.pop(i)
            return
    raise LookupError("Reserva não encontrada.")
