from controllers.sql import Banco

class Cliente:
    def __init__(self, usuario=None, senha=None):
        self.usuario = usuario
        self.senha = senha
        self.banco = Banco()

    def inserir_usuario(self):
        """Registra um novo usuário no banco"""
        try:
            dados = {'usuario': self.usuario, 'senha': self.senha}
            self.banco.inserir('tb_login', dados)
            print(f"Usuario {self.usuario} cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro ao cadastrar usu rio: {str(e)}")
    
    def logar(self, usuario, senha):
        try:
            resultado = self.banco.efetuar_login('tb_usuarios', usuario, senha)
            print(resultado)
            if resultado:
                print("Usuario.py | Validar Login | Login realizado com sucesso")
                return resultado  # Retorna os dados completos do usuário
            else:
                print("Usuario.py | Validar Login | Credenciais inválidas")
                return None
        except Exception as erro:
            print(f"Aconteceu o erro: {erro} ")

            print("Usuario.py | Validar Login | Erro ao validar login:")
            return None
