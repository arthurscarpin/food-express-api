from modelos.restaurante import Restaurante
import pyodbc

class RestauranteInserir(Restaurante):
    def executar(self):
        ativo = 1 if self.ativo else 0
        
        if not (self.nome and self.categoria):
            return {'mensagem': 'Os campos estão vazios.', 'sucesso': False}
        
        conexao = self.conectar()
        try:
            with conexao.cursor() as cursor:
                comando = "INSERT INTO Restaurante (nome_restaurante, categoria, status) VALUES (?, ?, ?)"
                cursor.execute(comando, (self.nome, self.categoria, ativo))
                conexao.commit()
                return {'mensagem': 'O restaurante foi cadastrado com sucesso.', 'sucesso': True}
        except pyodbc.Error as ex:
            return {'mensagem': f'Erro ao inserir restaurante: {str(ex)}', 'sucesso': False}
        finally:
            conexao.close()
