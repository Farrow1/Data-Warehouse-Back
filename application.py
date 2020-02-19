from flask import Flask,jsonify
from repos.classes import Customer, Agents, Loan, Transaction, Accounts, Card
from repos.db_conn import session



app = Flask(__name__)

@app.route("/")
def hello():
    return "Loren ipsum dolor sit amet"

@app.route("/api/customers/<id>")
def customers(id):
    customer = session.query(Customer).get(id)

    return jsonify([customer.customer_Id, customer.first_name, customer.last_name, customer.phone, customer.address, customer.agent_id])

@app.errorhandler(500)
def key_not_found(e):
    return "This Primary Key was not found"

if __name__ == "__main__":
    app.run()
