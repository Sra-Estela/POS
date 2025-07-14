from sqlmodel import SQLModel, create_engine

# Caminho do banco de dados
sqlite_url = "sqlite:///./pedidos.db"
engine = create_engine(sqlite_url, echo=False)

# Criar tabelas
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
