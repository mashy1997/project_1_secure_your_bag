from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.customer_transaction import CustomerTransaction
from models.merchant import Merchant
import repositories.customer_transaction_repository as customer_transaction_repository
import repositories.category_repository as category_repository 
import repositories.merchant_repository as merchant_repository 

customer_transactions_blueprint = Blueprint("customer_transactions", __name__)
# @app.before_request
# def before_request_func():
#     print("before_request executing!")
# @customer_transactions_blueprint.context_processor
# def total():
#     customer_transactions = customer_transaction_repository.select_all()
#     total_amount_spent = 0
#     for spent in customer_transactions:
#         total_amount_spent += spent.amount
#     return total_amount_spent

# @customer_transactions_blueprint.route("/")
# def home():
#     customer_transactions = customer_transaction_repository.select_all()
#     total_amount_spent = 0
#     for spent in customer_transactions:
#         total_amount_spent += spent.amount
#     return render_template("base.jinja", customer_transactions = customer_transactions, total_amount_spent = total_amount_spent)


@customer_transactions_blueprint.route("/customer_transactions")
def customer_transactions():
    customer_transactions = customer_transaction_repository.select_all()
    return render_template("customer_transactions/index.jinja", customer_transactions = customer_transactions)

#NEW, GET 'customer_transactions/new'
@customer_transactions_blueprint.route("/customer_transactions/new", methods = ['GET'])
def new_customer_transaction():
    categories = category_repository.select_all()
    merchants = merchant_repository.select_all()
    return render_template("customer_transactions/new.jinja", categories = categories, merchants = merchants)

#CREATE, POST '/customer_transactions'
@customer_transactions_blueprint.route("/customer_transactions", methods=['POST'])
def create_customer_transaction():
    description = request.form['description']
    amount = request.form['amount']
    merchant = merchant_repository.select(request.form['merchant'])
    category = category_repository.select(request.form['category'])
    customer_transaction = CustomerTransaction(description, amount, merchant, category)
    customer_transaction_repository.save(customer_transaction)
    return redirect('/customer_transactions')

#SHOW, GET '/customer_transactions/<id>'
@customer_transactions_blueprint.route("/customer_transactions/<id>", methods =['GET'])
def show_customer_transaction(id):
    customer_transaction = customer_transaction_repository.select(id)
    return render_template('customer_transactions/show.jinja', customer_transaction = customer_transaction)

#EDIT, GET 'customer_transactions/<id>/edit'
@customer_transactions_blueprint.route("/customer_transactions/<id>/edit", methods=['GET'])
def edit_customer_transaction(id):
    customer_transaction = customer_transaction_repository.select(id)
    merchants = merchant_repository.select_all()
    categories = category_repository.select_all()
    return render_template('/customer_transactions/edit.jinja', customer_transaction = customer_transaction, merchants = merchants, categories = categories)

#UPDATE, PUT '/customer_transactions/<id>'
@customer_transactions_blueprint.route("/customer_transactions/<id>", methods=['POST'])
def update_customer_transaction(id):
    description = request.form['description']
    amount = request.form['amount']
    merchant = merchant_repository.select(request.form['merchant_id'])
    category = category_repository.select(request.form['category_id'])
    customer_transaction = CustomerTransaction(description, amount, merchant, category, id)
    customer_transaction_repository.update(customer_transaction)
    return redirect(f'/customer_transactions/{id}')

#DELETE '/customer_transactions/<id>'
@customer_transactions_blueprint.route("/customer_transactions/<id>/delete", methods=['POST'])
def delete_customer_transaction(id):
    customer_transaction_repository.delete(id)
    return redirect('/customer_transactions')
