from fastapi import FastAPI
from app.routers import carros, clientes, reservas

app = FastAPI(title="Sistema de Reserva de Carros")

app.include_router(carros.router)
app.include_router(clientes.router)
app.include_router(reservas.router)
