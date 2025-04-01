from src.repository.operadoras_repo import OperadorasRepository

class OperadorasController:
    def __init__(self):
        self.repository = OperadorasRepository()

    def get_operadora(self, nome):
        operadora = self.repository.get_operadora(nome)
        if operadora:
            return operadora
        return None
    
    def get_operadoras(self):
        operadoras = self.repository.get_operadoras()
        if operadoras:
            return operadoras
        return None