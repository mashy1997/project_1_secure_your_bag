from db.run_sql import run_sql
from models.category import Category
from models.customer_transaction import CustomerTransaction
from models.merchant import Merchant

def save(category):
    sql = "INSERT INTO categories(name) VALUES (%s) RETURNING id"
    values = [category.name]
    results = run_sql( sql, values )
    id = results[0]['id']
    category.id = id
    return category

def select_all():
    categories = []

    sql = "SELECT * FROM categories"
    results = run_sql(sql)

    for row in results:
        category = Category(row['name'], row['id'])
        categories.append(category)
    return categories

def select(id):
    category = None
    sql = "SELECT * FROM categories WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result= results[0]
        category = Category(result['name'], result['id'])
    return category

def delete_all():
    sql = "DELETE FROM categories"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM categories WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(category):
    sql = "UPDATE categories SET name = %s where id=%s"
    values = [category.name, category.id]
    run_sql(sql, values)

# def add_all_amounts(amount):
#     total_amount = []

#     sql = "SELECT amount FROM categories"
