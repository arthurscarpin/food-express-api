from modelos.restaurante import Restaurante

class RestauranteExibir(Restaurante):
    def executar(self):
        conexao = self.conectar()
        try:
            with conexao.cursor() as cursor:
                comando = "SELECT * FROM Restaurante"
                cursor.execute(comando)
                linhas = cursor.fetchall()
                resultados = []
                for linha in linhas:
                    restaurante = {
                        'id_restaurante': linha.id_restaurante,
                        'nome_restaurante': linha.nome_restaurante,
                        'categoria': linha.categoria,
                        'status': 1 if linha.status else 0,
                        'avaliacao': linha.avaliacao if linha.avaliacao else 0
                    }
                    resultados.append(restaurante)
                return resultados
        except:
            return None
        finally:
            conexao.close()