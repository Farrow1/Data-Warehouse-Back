import pyodbc
import urllib
from sqlalchemy.engine import url, create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy

db_url = urllib.parse.quote_plus
(r'Driver={ODBC Driver 13 for SQL Server};Server=tcp:csc439.database.windows.net,1433;Database=datawarehouse;Uid=allenj25;Pwd=Jack1998;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    
conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(db_url)
engine = create_engine(conn_str)

test= "please for the love of god work"

Session = sessionmaker(bind = engine)

session = Session()
