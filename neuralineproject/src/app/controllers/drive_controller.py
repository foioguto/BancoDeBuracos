from flask import Blueprint, request, jsonify
from .models import User
from . import db

main = Blueprint('main', __name__)

@main.route('/usuario', methods=['POST'])
def create_user():
    name = request.json.get('nome')
    new_user = User(nome=name)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"mensagem": "Usuário criado com sucesso"}), 201

@main.route('/usuarios', methods=['GET'])
def list_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "nome": u.name} for u in users])
