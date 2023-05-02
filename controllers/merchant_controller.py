from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
import repositories.category_repository as category_repository
import repositories.customer_transaction_repository as customer_transaction_repository
import repositories.merchant_repository as merchant_repository

merchants_blueprint = Blueprint("merchants", __name__)

@merchants_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all()
    return render_template("merchants/index.jinja", merchants = merchants)

#NEW, GET '/merchants/new'
@merchants_blueprint.route("/merchants/new", methods = ['GET'])
def new_merchant():
    return render_template("merchants/new.jinja")
