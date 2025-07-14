from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select
from app.models import Pedido
from app.database import engine, create_db_and_tables

app = FastAPI()

@app.on_event("startup")
def startup_event():
    create_db_and_tables()

@app.get("/pedido/{id}")
def get_pedido(id: int):
    with Session(engine) as session:
        pedido = session.exec(select(Pedido).where(Pedido.IdPedido == id)).first()
        if not pedido:
            raise HTTPException(status_code=404, detail="Pedido não encontrado")
        return pedido
