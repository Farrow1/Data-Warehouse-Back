from repos.db_conn import session
from sqlalchemy import Column, Integer, String, Float, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'Customer'

    customer_Id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    phone = Column(Integer)
    address = Column(String)
    agent_id= Column(Integer)

    def __init__(self, customer_Id, first_name, last_name, phone, address, agent_id):
        self.customer_Id = customer_Id
        self.firstName = first_name
        self.lastName = last_name
        self.phone = phone
        self.address = address
        self.agent_id = agent_id

class Accounts(Base):
    __tablename__ = 'Accounts'

    accountID = Column(Integer, primary_key=True)
    customerID = Column(Integer)
    balance = Column(Float)
    interest = Column(Float)
    isInvestment = Column(Boolean)
    pin = Column(Integer)


    def __init__(self, accountID, customerID, balance, interest, isInvestment, pin):
        self.accountID = accountID
        self.customerID = customerID
        self.balance = balance
        self.interest = interest
        self.isInvestment = isInvestment
        self.pin = pin

class Transaction(Base):
    __tablename__ = 'Transation'

    trasactionID = Column(Integer, primary_key=True)
    date = Column(Date)
    amount = Column(Float)
    accountID = Column(Integer)
    source = Column(Integer)
    destination = Column(Integer)

    def __init__(self, transactionID, date, amount, accountID, source, destination):
        self.transactionID = transactionID
        self.date = date
        self.amount = amount
        self.accountID = accountID
        self.source = source
        self.destination = destination

class Card(Base):
    __tablename__ = 'Card'

    cardNumber = Column(Integer, primary_key=True)
    accountID = Column(Integer)
    cardType = Column(String)

    def __init__(self, cardNumber, accountID, cardType):
        self.cardNumber = cardNumber
        self.accountID = accountID
        self.cardType = cardType

class Agents(Base):
    __tablename__ = 'Agents'

    agentId = Column(Integer, primary_key=True)
    firstName = Column(String)
    lastName = Column(String)

    def __init__(self, agentId, firstName, lastName):
        self.agentId = agentId
        self.firstName = firstName
        self.lastName = lastName

class Loan(Base):
    __tablename__ = 'Loan'

    loanId = Column(Integer, primary_key=True)
    accountId = Column(Integer)
    amount = Column(Float)
    interest = Column(Float)

    def __init__(self, loanId, accountId, amount, interest):
        self.loadId = loanId
        self.accountId = accountId
        self.amount = amount
        self.interest = interest