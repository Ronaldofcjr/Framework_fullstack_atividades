class User:
       
       def __init__(self, nome, email, senha, cpf):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cpf = cpf

        def to_dict(self):
            
            return {
                'nome': self.nome,
                'email': self.email,
                'senha': self.senha,
                'cpf': self.cpf
            }
