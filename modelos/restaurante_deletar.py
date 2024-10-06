from modelos.restaurante import Restaurante
from modelos.restaurante_filtrar import RestauranteFiltrar
import pyodbc

class RestauranteDeletar(Restaurante):

    def executar(self, id):
        restaurante = RestauranteFiltrar().executar(id)
        if restaurante and restaurante['id_restaurante']:
            conexao = self.conectar()
            if conexao:
                try:
                    with conexao.cursor() as cursor:
                        comando = "DELETE FROM Restaurante WHERE id_restaurante = ?"
                        cursor.execute(comando, (id,))
                        conexao.commit()
                        return {'mensagem': 'Restaurante deletado com sucesso.', 'sucesso': True}
                except pyodbc.Error as ex:
                    return {'mensagem': f'Erro ao deletar o restaurante: {str(ex)}', 'sucesso': False}
                finally:
                    conexao.close()
            else:
                return {'mensagem': 'Erro ao conectar ao banco de dados.', 'sucesso': False}
        else:
            return {'mensagem': 'O restaurante não foi encontrado.', 'sucesso': False}