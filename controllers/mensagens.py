from controllers.sql import Banco

class Mensagem:
    def __init__(self, texto, data_envio, nome_usuario):
        self.texto = texto
        self.data_envio = data_envio
        self.nome_usuario = nome_usuario
        self.banco = Banco()

    def inserir_mensagem(self):
        try:
            dados = {'texto': self.texto, 'data_envio': self.data_envio, 'nome_usuario': self.nome_usuario}
            self.banco.inserir('tb_mensagens', dados)
            print(f"cadastrada com sucesso!")

        except Exception as e:
            print(f"Erro ao cadastrar usuario: {str(e)}")
    def carregar_mensagens(self):
        try:
            self.banco.conectar()
            sql = f"SELECT texto, nome_usuario, strftime('%d/%m/%Y - %Hh%M', data_envio) AS data_formatada FROM TB_MENSAGENS"

            self.banco.cursor.execute(sql)

            resultado = self.banco.cursor.fetchall()

            self.banco.desconectar()        
           
            return resultado
        except Exception as e:
            print("Erro ao listar as mensagens:", e)
            return None
        
    # def carregar_minhas_mensagens(self):
    #     try:
    #         self.banco.conectar()
    #         sql = f"SELECT texto, nome_usuario, strftime('%d/%m/%Y - %Hh%M', data_envio) AS data_formatada FROM TB_MENSAGENS where nome_usuario  = '{self.nome_usuario}'"

    #         self.banco.cursor.execute(sql)

    #         resultado = self.banco.cursor.fetchall()

    #         self.banco.desconectar()        
           
    #         return resultado
    #     except Exception as e:
    #         print("Erro ao listar as mensagens:", e)
    #         return None
