from abc import ABC, abstractmethod
from banco.conexao_banco import ConexaoBanco

class Restaurante(ABC):
    def __init__(self, nome=None, categoria=None):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
    
    @staticmethod
    def conectar():
        return ConexaoBanco().conectar()
    
    @abstractmethod
    def executar(self):
        pass
    