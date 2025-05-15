from flask import Blueprint, request, jsonify
from .models import Usuario
from . import db

main = Blueprint('main', __name__)

@main.route('/usuario', methods=['POST'])
def create_user():
    nome = request.json.get('nome')
    novo_usuario = Usuario(nome=nome)
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({"mensagem": "Usuário criado com sucesso"}), 201

@main.route('/usuarios', methods=['GET'])
def list_users():
    usuarios = Usuario.query.all()
    return jsonify([{"id": u.id, "nome": u.nome} for u in usuarios])
