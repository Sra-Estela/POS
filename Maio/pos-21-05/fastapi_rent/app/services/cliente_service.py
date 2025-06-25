from app.database import clientes
from app.models import Cliente

def listar_clientes():
    return clientes

def adicionar_cliente(cliente: Cliente):
    if any(c.id == cliente.id for c in clientes):
        raise ValueError("ID de cliente já existe.")
    clientes.append(cliente)
    return cliente

def buscar_cliente(id: int):
    for c in clientes:
        if c.id == id:
            return c
    raise LookupError("Cliente não encontrado.")
