from modelos.restaurante import Restaurante
from modelos.restaurante_filtrar import RestauranteFiltrar
import pyodbc

class RestauranteAvaliar(Restaurante):
    
    def executar(self, id, nota):
        conexao = self.conectar()
        restaurante = RestauranteFiltrar().executar(id)
        print(restaurante)

        if restaurante:
            avaliacao_atual = restaurante['avaliacao']
            status = restaurante['status']
            if 0 <= nota <= 5:
                notas = []
                notas.append(nota)
                if avaliacao_atual != 0 and avaliacao_atual is not None:
                    notas.append(avaliacao_atual)
                media = sum(notas) / len(notas)
                if status == True:
                    conexao = self.conectar()
                    if conexao:
                        try:
                            with conexao.cursor() as cursor:
                                comando = "UPDATE Restaurante SET avaliacao = ? WHERE id_restaurante = ?"
                                cursor.execute(comando, (media, id))
                                conexao.commit()
                                return {'mensagem': 'Avaliação efetuada com sucesso.', 'sucesso': True}
                        except pyodbc.Error as ex:
                            return {'mensagem': f'Erro ao efetuar a avaliação: {str(ex)}', 'sucesso': False}
                        finally:
                            conexao.close()
                    else:
                        return {'mensagem': 'Erro ao conectar ao banco de dados.', 'sucesso': False}
                else:
                    return {'mensagem': 'O restaurante está desativado.', 'sucesso': False}
            else:
                return {'mensagem': 'A nota é inválida.', 'sucesso': False}
        else:
            return {'mensagem': 'O restaurante não foi encontrado.', 'sucesso': False}
        