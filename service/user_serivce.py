from model import user

banco = [ {
    'nome': 'Ronaldo',
    'email': 'ronaldo.cavalcante94@gmail.com',
    'senha': '123456',
    'cpf': '123.456.789-00'
}]


class UserService:

    @staticmethod
    def criar_usuario(dados):
        campos_necessarios = ['nome', 'email', 'senha', 'cpf']
        for campo in campos_necessarios:
            if campo not in dados:
                raise ValueError(f"Campo '{campo}' é obrigatório.")
            
        for usuario in banco:
            if usuario['cpf'] == dados['cpf']:
                raise ValueError("CPF já cadastrado.")
            
        banco.append(dados)
        return {"mensagem": "Usuário criado com sucesso."}
            
    @staticmethod
    def listar_usuarios():
        return banco
    
    @staticmethod
    def buscar_usuario_por_cpf(cpf):
        for usuario in banco:
            if usuario['cpf'] == cpf:
                return usuario
            
        return{'error': 'Usuário não encontrado.'}
    
    @staticmethod
    def deletar_usuario(cpf):
        for usuario in banco:
            if usuario['cpf'] == cpf:
                banco.remove(usuario)
                return {"mensagem": "Usuário deletado com sucesso."}
            
        return {'error': 'Usuário não encontrado.'}
    
    
            

