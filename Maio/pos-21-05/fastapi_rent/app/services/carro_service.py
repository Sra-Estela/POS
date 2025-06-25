from app.database import carros
from app.models import Carro

def listar_carros():
    return carros

def listar_disponiveis():
    return [c for c in carros if c.disponivel]

def adicionar_carro(carro: Carro):
    if any(c.id == carro.id for c in carros):
        raise ValueError("ID de carro já existe.")
    carros.append(carro)
    return carro

def atualizar_carro(id: int, carro: Carro):
    for i, c in enumerate(carros):
        if c.id == id:
            carros[i] = carro
            return carro
    raise LookupError("Carro não encontrado.")

def remover_carro(id: int):
    for i, c in enumerate(carros):
        if c.id == id:
            carros.pop(i)
            return
    raise LookupError("Carro não encontrado.")
