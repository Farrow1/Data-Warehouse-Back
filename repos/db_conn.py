from sqlalchemy.connectors import pyodbc
import urllib
from sqlalchemy.engine import url, create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy

server='tcp:csc439.database.windows.net'
database='datawarehouse'
username = 'allenj25'
password = 'Jack1998'
driver = '{ODBC Driver 17 for SQL Server}'
cnxn = ('DRIVER=' + driver + ';SERVER='+server+',1433;DATABASE='+database+';UID='+username+';PWD='+password)

connect_str = 'mssql+pyodbc:///?odbc_connect=' + urllib.parse.quote_plus(cnxn) + "?driver=SQL+Server"
engine = create_engine(connect_str)

Session = sessionmaker(bind = engine)

session = Session()
