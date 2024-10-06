import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

class ConexaoBanco:
    def __init__(self):
        self._driver = os.getenv('DB_DRIVER')
        self._server = os.getenv('DB_SERVER')
        self._banco = os.getenv('DB_NAME')
        self._conexao = None

    def conectar(self):
        dados_conexao = (
            f"Driver={self._driver};"
            f"Server={self._server};"
            f"Database={self._banco};"
        )
        try:
            self._conexao = pyodbc.connect(dados_conexao)
            return self._conexao
        except pyodbc.Error as ex:
            return None