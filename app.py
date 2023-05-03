from flask import Flask, render_template

from controllers.customer_transaction_controller import customer_transactions_blueprint
from controllers.merchant_controller import merchants_blueprint
from controllers.category_controller import categories_blueprint
import repositories.customer_transaction_repository as customer_transaction_repository

app = Flask(__name__)

app.register_blueprint(customer_transactions_blueprint)
app.register_blueprint(merchants_blueprint)
app.register_blueprint(categories_blueprint)

@app.context_processor
def total():
    customer_transactions = customer_transaction_repository.select_all()
    total_amount_spent = 0
    for spent in customer_transactions:
        total_amount_spent += spent.amount
    return {'total_amount':total_amount_spent}

@app.route('/')
def home():

    return render_template('index.jinja')

if __name__ == '__main__':
    app.run(debug=True)