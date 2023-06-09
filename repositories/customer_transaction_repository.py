from db.run_sql import run_sql

from models.customer_transaction import CustomerTransaction
from models.category import Category
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository 
import repositories.category_repository as category_repository 

def save(customer_transaction):
    sql = "INSERT INTO customer_transactions (description, amount, merchant_id, category_id) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [customer_transaction.description, customer_transaction.amount, customer_transaction.merchant.id, customer_transaction.category.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    customer_transaction.id = id
    return customer_transaction

def select_all():
    customer_transactions = []

    sql = "SELECT * FROM customer_transactions"
    results = run_sql(sql)

    for row in results:
        category = category_repository.select(row['category_id'])
        merchant = merchant_repository.select(row['merchant_id'])
        customer_transaction = CustomerTransaction(row['description'], row['amount'], merchant, category, row['id'])
        customer_transactions.append(customer_transaction)
    return customer_transactions

def select(id):
    customer_transaction = None
    sql = "SELECT * FROM customer_transactions WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        merchant = merchant_repository.select(result['merchant_id'])
        category = category_repository.select(result['category_id'])
        customer_transaction = CustomerTransaction(result['description'], result['amount'], merchant, category, result['id'])
    return customer_transaction

def delete_all():
    sql = "DELETE FROM customer_transactions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM customer_transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(customer_transaction):
    sql = "UPDATE customer_transactions SET (description, amount, merchant_id, category_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [customer_transaction.description, customer_transaction.amount, customer_transaction.merchant.id, customer_transaction.category.id, customer_transaction.id]
    run_sql(sql, values)

#def get_total_amount(amount):
#   sql = "SELECT amount FROM customer_transactions"
#   values = [customer_transaction.description]
#   results = run_sql(sql, values)

#   for row in results:
#   amount = customer_transactions_repository.select(result['amount'])