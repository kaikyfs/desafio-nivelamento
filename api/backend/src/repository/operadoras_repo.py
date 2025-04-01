from sqlalchemy import create_engine, MetaData, Table
from src.model.operadora import Operadora
from config import DATABASE_URL

class OperadorasRepository:
    def __init__(self):
        if not DATABASE_URL:
            raise ValueError("DATABASE_URL is not set")
        
        self.engine = create_engine(DATABASE_URL)
        self.metadata = MetaData()
        self.operadoras_table = Table('operadoras_plano_saude', self.metadata, autoload_with=self.engine)

    def get_operadora(self, nome):
        with self.engine.connect() as conn:
            query = self.operadoras_table.select().where(self.operadoras_table.c.nome_fantasia == nome.upper())
            result = conn.execute(query).fetchone()
            if result:
                operadora_dict = result._asdict()
                return Operadora(**operadora_dict)
            return None
        
    def get_operadoras(self):
        with self.engine.connect() as conn:
            query = self.operadoras_table.select()
            results = conn.execute(query).fetchall()
            operadoras = [Operadora(**row._asdict()) for row in results]
            return operadoras