from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.customer_transaction import CustomerTransaction
import repositories.customer_transaction_repository as customer_transaction_repository
import repositories.category_repository as category_repository 
import repositories.merchant_repository as merchant_repository 

customer_transactions_blueprint = Blueprint("customer_transactions", __name__)

@customer_transactions_blueprint.route("/customer_transactions")
def customer_transactions():
    customer_transactions = customer_transaction_repository.select_all()
    return render_template("customer_transactions/index.html", customer_transactions = customer_transactions)