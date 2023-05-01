from db.run_sql import run_sql
from models.category import Category
from models.merchant import Merchant
from models.customer_transaction import CustomerTransaction

def save(merchant):
    sql = "INSERT INTO merchants (name) VALUES (%s) RETURNING id"
    values = [merchant.name]
    results = run_sql(sql, values)
    merchant.id = results[0]['id']
    return merchant

def select_all():
    merchants = []

    sql = "SELECT * FROM merchants"
    results = run_sql(sql)

    for row in results:
        merchant = Merchant(row['name'], row['id'])
        merchants.append(merchant)
    return merchants

def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        merchant = Merchant(result['name'], result['id'])
    return merchant

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)