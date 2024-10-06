from modelos.restaurante import Restaurante

class RestauranteFiltrar(Restaurante):
    def executar(self, id):
        conexao = self.conectar()
        try:
            with conexao.cursor() as cursor:
                comando = "SELECT * FROM Restaurante WHERE id_restaurante = ?"
                cursor.execute(comando, (id,))
                restaurante = cursor.fetchone()
                if restaurante:
                    return {
                        'id_restaurante': restaurante.id_restaurante,
                        'nome_restaurante': restaurante.nome_restaurante,
                        'categoria': restaurante.categoria,
                        'status': restaurante.status,
                        'avaliacao': restaurante.avaliacao
                        }
                else:
                    return None
        except:
            return None
        