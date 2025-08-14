from .extensions import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    transactions = db.relationship('Transaction', backref='owner', lazy=True, cascade="all")

def set_password(self, password):
    self.password_hash = generate_password_hash(password)

def check_password(self, password):
    #Verifica se a senha fornecida corresponde à senha armazenada.
    return check_password_hash(self.password_hash, password)

def to_dict(self):
    return {
        "id": self.id,
        "username": self.username,
        "created_at": self.created_at,
        "total_transactions": len(self.transactions)
    }

class Transaction(db.Model):
    __tablename__ = "transactions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(200), nullable=True)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    type = db.Column(db.String(10), nullable=False, index=True)  # 'income' or 'expense'
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "amount": self.amount,
            "type": self.type,
            "date": self.date,
            "user_id": self.user_id
        }