# arquivo: main.py
from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

# Carregar o CSV uma vez na inicialização
df = pd.read_csv("20250702_Pedidos_csv_2025.csv", sep=';', encoding='utf-16')

@app.get("/pedido/{id_pedido}")
def get_pedido(id_pedido: int):
    pedido = df[df["IdPedido"] == id_pedido]
    if pedido.empty:
        raise HTTPException(status_code=404, detail="Pedido não encontrado.")
    
    # Retornar como dicionário (omitindo o index)
    return pedido.iloc[0].to_dict()
