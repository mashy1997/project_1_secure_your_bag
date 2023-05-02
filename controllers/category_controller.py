from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.category import Category
import repositories.category_repository as category_repository
import repositories.customer_transaction_repository as customer_transaction_repository
import repositories.merchant_repository as merchant_repository

categories_blueprint = Blueprint("categories", __name__)

@categories_blueprint.route("/categories", methods=['GET'])
def merchants():
    categories = category_repository.select_all()
    return render_template("categories/index.jinja", categories = categories)

#NEW, GET '/categories/new'
@categories_blueprint.route("/categories/new", methods = ['GET'])
def new_category():
    return render_template("categories/new.jinja")

#CREATE, POST 'merchants'
@categories_blueprint.route("/categories", methods = ['POST'])
def create_category():
    name = request.form['name']
    category = Category(name)
    category_repository.save(category)
    return redirect('/categories')

#DELETE, '/categories/<id>'
@categories_blueprint.route("/categories/<id>/delete", methods = ['POST'])
def delete_category(id):
    category_repository.delete(id)
    return redirect('/categories')
