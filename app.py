from flask import Flask, render_template

from controllers.customer_transaction_controller import customer_transactions_blueprint
from controllers.merchant_controller import merchants_blueprint

app = Flask(__name__)

app.register_blueprint(customer_transactions_blueprint)
app.register_blueprint(merchants_blueprint)

@app.route('/')
def home():
    return render_template('index.jinja')

if __name__ == '__main__':
    app.run(debug=True)