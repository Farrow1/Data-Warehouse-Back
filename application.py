from flask import Flask
#from repos.classes import Customer, Agents, Loan, Transaction, Accounts, Card

#from repos.db_conn import test

app = Flask(__name__)

@app.route("/")
def hello():
    return "Loren ipsum dolor sit amet"

@app.route("/test", methods=['GET'])
def testtwo():
    return "Is this working"

