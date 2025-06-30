from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class Veiculo(BaseModel):
    nome: str
    marca: str
    modelo: str
    placa: str

# "Banco de dados" em memória
banco_veiculos: Dict[str, Veiculo] = {}

@app.post("/veiculos")
def cadastrar_veiculo(veiculo: Veiculo):
    if veiculo.placa in banco_veiculos:
        raise HTTPException(status_code=400, detail="Placa já cadastrada.")
    banco_veiculos[veiculo.placa] = veiculo
    return {"mensagem": "Veículo cadastrado com sucesso."}

@app.get("/veiculos")
def listar_veiculos():
    return list(banco_veiculos.values())

@app.get("/veiculos/{placa}")
def obter_veiculo(placa: str):
    if placa not in banco_veiculos:
        raise HTTPException(status_code=404, detail="Veículo não encontrado.")
    return banco_veiculos[placa]

@app.put("/veiculos/{placa}")
def atualizar_veiculo(placa: str, veiculo: Veiculo):
    if placa not in banco_veiculos:
        raise HTTPException(status_code=404, detail="Veículo não encontrado.")
    if veiculo.placa != placa and veiculo.placa in banco_veiculos:
        raise HTTPException(status_code=400, detail="Nova placa já está em uso.")
    del banco_veiculos[placa]
    banco_veiculos[veiculo.placa] = veiculo
    return {"mensagem": "Veículo atualizado com sucesso."}

@app.delete("/veiculos/{placa}")
def deletar_veiculo(placa: str):
    if placa not in banco_veiculos:
        raise HTTPException(status_code=404, detail="Veículo não encontrado.")
    del banco_veiculos[placa]
    return {"mensagem": "Veículo removido com sucesso."}
