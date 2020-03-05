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

@app.route("/api/account/<id>")
def accounts(id):
    account = session.query(Accounts).get(id)

    return jsonify([account.accountID, account.customerID, account.balance, account.interest, account.isIvestment, account.pin])

@app.route("/api/transaction/<id>")
def transaction(id):
    transaction = session.query(Transaction).get(id)

    return jsonify([transaction.transactionID, transaction.date, transaction.amount, transaction.source, transaction.destination])

@app.route("/api/card/<number>")
def card(number):
    card = session.query(Card).get(number)

    return jsonify([card.cardNumber, card.accountID, card.cardType])

@app.route("/api/loan/<id>")
def loan(id):
    loan = session.query(Loan).get(id)

    return jsonify([loan.loanId, loan.accountId, loan.amount, loan.interest])

@app.route("/api/agents/<id>")
def agents(id):
    agents = session.query(Agents).get(id)

    return jsonify([agents.agentId, agents.firstName, agents.lastName])


@app.errorhandler(500)
def key_not_found(e):
    return "This Primary Key was not found"

if __name__ == "__main__":
    app.run()
