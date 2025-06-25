from pydantic import BaseModel
from datetime import date

# -------- Carro ---------
class CarroBase(BaseModel):
    modelo: str
    marca: str
    ano: int
    disponivel: bool = True

class CarroCreate(CarroBase):
    pass

class CarroResponse(CarroBase):
    id: int

# -------- Cliente ---------
class ClienteBase(BaseModel):
    nome: str
    cpf: str
    telefone: str

class ClienteCreate(ClienteBase):
    pass

class ClienteResponse(ClienteBase):
    id: int

# -------- Reserva ---------
class ReservaBase(BaseModel):
    cliente_id: int
    carro_id: int
    data_inicio: date
    data_fim: date

class ReservaCreate(ReservaBase):
    pass

class ReservaResponse(ReservaBase):
    id: int
