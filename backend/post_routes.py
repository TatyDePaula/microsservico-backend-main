# backend/post_routes.py
from flask import jsonify, request, Blueprint
from backend import database
from backend.models import Post
from flask_cors import CORS

post_bp = Blueprint('post_bp', __name__)

@post_bp.route('/posts', methods=['GET'])
def get_posts():
    print('Rota /posts acessada')
    posts = Post.query.all()
    print(f'Número de posts encontrados: {len(posts)}')
    return jsonify([{
        'id': p.id,
        'titulo': p.titulo,
        'corpo': p.corpo,
        'data_criacao': p.data_criacao,
        'id_usuario': p.id_usuario
    } for p in posts])

@post_bp.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify({
        'id': post.id,
        'titulo': post.titulo,
        'corpo': post.corpo,
        'data_criacao': post.data_criacao,
        'id_usuario': post.id_usuario
    })

@post_bp.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    new_post = Post(
        titulo=data['titulo'],
        corpo=data['corpo'],
        id_usuario=data['id_usuario']
    )
    database.session.add(new_post)
    database.session.commit()
    return jsonify({'message': 'Post criado com sucesso!'}), 201

@post_bp.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    post = Post.query.get_or_404(id)
    data = request.get_json()
    post.titulo = data.get('titulo', post.titulo)
    post.corpo = data.get('corpo', post.corpo)
    database.session.commit()
    return jsonify({'message': 'Post atualizado com sucesso!'})

@post_bp.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = Post.query.get_or_404(id)
    database.session.delete(post)
    database.session.commit()
    return jsonify({'message': 'Post excluído com sucesso!'})
