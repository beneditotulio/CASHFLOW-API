from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.utils import calculate_balance
from  .models import Transaction
from .extensions import db
from .security import (register_user, login_user, get_user_profile, update_user_profile, delete_user_profile)

api = Blueprint('api', __name__)

#rota de autenticação
@api.route('/register', methods=['POST'])
def register():
    return register_user()

@api.route('/login', methods=['POST'])
def login():
    return login_user() 

#rotas de perfil do usuário
@api.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    return get_user_profile()

#rota de atualização de perfil
@api.route('/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    return update_user_profile()

#rota de exclusão de perfil
@api.route('/profile', methods=['DELETE'])
@jwt_required()
def delete_profile():
    return delete_user_profile()

#rota para transações
@api.route('/transactions', methods=['GET'])
@jwt_required()
def create_transaction():
    current_user_id = int(get_jwt_identity())
    data = request.get_json()

    if not all(key in data for key in ('description', 'amount', 'type')):
        return jsonify({"msg": "Missing fields"}), 400

    if data['type'] not in ['income', 'expense']:
        return jsonify({"msg": "The type must be 'income' or 'expense'"}), 400


@api.route('/transactions', methods=['GET'])
@jwt_required()
def get_transactions():
    current_user_id = int(get_jwt_identity())
    transactions = Transaction.query.filter_by(user_id=current_user_id).order_by(Transaction.date.desc()).all()
    return jsonify([t.to_dict() for t in transactions]), 200

@api.route('/transactions/<int:transaction_id>', methods=['PUT'])
@jwt_required()
def get_transaction(transaction_id):
    current_user_id = int(get_jwt_identity())
    transaction = Transaction.query.get_or_404(transaction_id)

    if transaction.user_id != current_user_id:
        return jsonify({"msg": "Unauthorized"}), 403
    return jsonify(transaction.to_dict()), 200

@api.route('/transactions/<int:transaction_id>', methods=['DELETE'])
@jwt_required()     
def delete_transaction(transaction_id):
    current_user_id = int(get_jwt_identity())
    transaction = Transaction.query.get_or_404(transaction_id)

    if transaction.user_id != current_user_id:
        return jsonify({"msg": "Unauthorized"}), 403

    db.session.delete(transaction)
    db.session.commit()
    return jsonify({"msg": "Transaction deleted successfully"}), 200

@api.route("/transactions/<int:transaction_id>", methods=['PUT'])
@jwt_required()
def update_transaction(transaction_id):
    current_user_id = int(get_jwt_identity())
    transaction = Transaction.query.get_or_404(transaction_id)
    if transaction.user_id != current_user_id:
        return jsonify({"msg": "Unauthorized"}), 403        

    data = request.get_json()
    transaction.description = data.get('description', transaction.description)
    transaction.amount = data.get('amount', transaction.amount)
    db.session.commit()
    return jsonify(transaction.to_dict()), 200

@api.route('/transaction/details/<int:transaction_id>', methods=['DELETE'])
@jwt_required()
def delete_transaction(transaction_id):
    current_user_id = int(get_jwt_identity())
    transaction = Transaction.query.get_or_404(transaction_id)

    if transaction.user_id != current_user_id:
        return jsonify({"msg": "Unauthorized"}), 403

    db.session.delete(transaction)
    db.session.commit()
    return jsonify({"msg": "Transaction deleted successfully"}), 200

#rota para saldo ou balance
@api.route('/balance', methods=['GET'])
@jwt_required()
def get_balance():
    current_user_id = int(get_jwt_identity())
    balance = calculate_balance(current_user_id)
    return jsonify({"balance": balance}), 200
