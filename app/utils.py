from .models import Transaction

def calculate_balance(user_id):
    transactions = Transaction.query.filter_by(user_id=user_id).all()

    total_balance = 0.0
    for t in transactions:
        if t.type == 'income':
            total_balance += float(t.amount)
        elif t.type == 'expense':
            total_balance -= float(t.amount)
    return round(total_balance, 2)