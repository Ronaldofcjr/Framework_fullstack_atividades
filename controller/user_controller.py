from flask import blueprints, request, jsonify
from service import user_serivce


user_bp = blueprints.Blueprint('user_bp', __name__)


class UserController:
    @staticmethod
    @user_bp.route('/usuarioscriar', methods=['POST'])
    def criar_usuario():
        dados = request.json
        try:
            resultado = user_serivce.UserService.criar_usuario(dados)
            return jsonify(resultado), 201
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        
    @staticmethod
    @user_bp.route('/usuarioslistar', methods=['GET'])
    def listar_usuarios():
        resultado = user_serivce.UserService.listar_usuarios()
        return jsonify(resultado), 200
    
    @staticmethod
    @user_bp.route('/usuariosbuscar/<cpf>', methods=['GET'])
    def buscar_usuario_por_cpf(cpf):
        resultado = user_serivce.UserService.buscar_usuario_por_cpf(cpf)
        if 'error' in resultado:
            return jsonify(resultado), 404
        return jsonify(resultado), 200
    
    @staticmethod
    @user_bp.route('/usuariosdeletar/<cpf>', methods=['DELETE'])
    def deletar_usuario(cpf):
        resultado = user_serivce.UserService.deletar_usuario(cpf)
        if 'error' in resultado:
            return jsonify(resultado), 404
        return jsonify(resultado), 200
    






