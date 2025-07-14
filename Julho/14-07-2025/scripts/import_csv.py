import pandas as pd
from sqlmodel import Session
from app.database import engine
from app.models import Pedido

# Lê o CSV
df = pd.read_csv("data/pedidos.csv", sep=";", dtype=str)
df["DataRegistro"] = pd.to_datetime(df["DataRegistro"], dayfirst=True, errors='coerce')
df["PrazoAtendimento"] = pd.to_datetime(df["PrazoAtendimento"], dayfirst=True, errors='coerce')
df["DataResposta"] = pd.to_datetime(df["DataResposta"], dayfirst=True, errors='coerce')

# Corrige tipos
df = df.where(pd.notnull(df), None)
df["IdPedido"] = df["IdPedido"].astype(int)
df["IdSolicitante"] = pd.to_numeric(df["IdSolicitante"], errors="coerce").fillna(0).astype(int)

# Insere no banco
with Session(engine) as session:
    for _, row in df.iterrows():
        pedido = Pedido(**row.to_dict())
        session.add(pedido)
    session.commit()

print("Dados importados com sucesso!")
