from modelos.restaurante import Restaurante
from modelos.restaurante_filtrar import RestauranteFiltrar
import pyodbc

class RestauranteAlternarStatus(Restaurante):

    def executar(self, id):
        restaurante = RestauranteFiltrar().executar(id)
        if restaurante:
            conexao = self.conectar()
            status = 1 if not restaurante['status'] else 0 
            if conexao:
                try:
                    with conexao.cursor() as cursor:
                        comando = "UPDATE Restaurante SET status = ? WHERE id_restaurante = ?"
                        cursor.execute(comando, (status, id))
                        conexao.commit()
                        return {'mensagem': 'O estado foi alterado com sucesso.', 'sucesso': True}
                except pyodbc.Error as ex:
                    return {'mensagem': f'Erro ao alterar o estado do restaurante: {str(ex)}', 'sucesso': False}
                finally:
                    conexao.close()
            else:
                return {'mensagem': 'Erro ao conectar ao banco de dados.', 'sucesso': False}
        else:
            return {'mensagem': 'O restaurante não foi encontrado.', 'sucesso': False}