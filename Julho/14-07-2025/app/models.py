from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class Pedido(SQLModel, table=True):
    IdPedido: int = Field(primary_key=True)
    ProtocoloPedido: str
    Esfera: str
    UF: Optional[str]
    Municipio: Optional[str]
    OrgaoDestinatario: str
    Situacao: str
    DataRegistro: Optional[date]
    PrazoAtendimento: Optional[date]
    FoiProrrogado: str
    FoiReencaminhado: str
    FormaResposta: str
    OrigemSolicitacao: str
    IdSolicitante: int
    AssuntoPedido: str
    SubAssuntoPedido: str
    Tag: Optional[str]
    DataResposta: Optional[date]
    Decisao: Optional[str]
    EspecificacaoDecisao: Optional[str]
