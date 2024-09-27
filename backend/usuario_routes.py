# backend/usuario_routes.py
from flask import jsonify, request, Blueprint
from backend import database
from backend.models import Usuario

usuario_bp = Blueprint('usuario_bp', __name__)

@usuario_bp.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{
        'id': u.id,
        'username': u.username,
        'email': u.email,
        'cep': u.cep,
        'endereco': u.endereco,
        'cursos': u.cursos
    } for u in usuarios])

@usuario_bp.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    return jsonify({
        'id': usuario.id,
        'username': usuario.username,
        'email': usuario.email,
        'cep': usuario.cep,
        'endereco': usuario.endereco,
        'cursos': usuario.cursos
    })

@usuario_bp.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.get_json()
    print(data)
    new_user = Usuario(
        username=data['username'],
        email=data['email'],
        cep=data['cep'],
        endereco=data['endereco'],
        senha=data['senha'],
        cursos=data['cursos']
    )
    database.session.add(new_user)
    database.session.commit()
    return jsonify({'message': 'Usuario criado com sucesso!'}), 201

@usuario_bp.route('/usuarios/<int:id>', methods=['PUT'])
def update_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    data = request.get_json()
    usuario.username = data.get('username', usuario.username)
    usuario.email = data.get('email', usuario.email)
    usuario.cep = data.get('cep', usuario.cep)
    usuario.endereco = data.get('endereco', usuario.endereco)
    usuario.cursos = data.get('cursos', usuario.cursos)
    database.session.commit()
    return jsonify({'message': 'Usuario atualizado com sucesso!'})

@usuario_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    database.session.delete(usuario)
    database.session.commit()
    return jsonify({'message': 'Usuario excluído com sucesso!'})
