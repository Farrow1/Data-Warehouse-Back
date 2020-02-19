from sqlalchemy.connectors import pyodbc
import urllib
from sqlalchemy.engine import url, create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy

# db_url = urllib.parse.quote_plus
# (r'Driver={ODBC Driver 13 for SQL Server};Server=tcp:csc439.database.windows.net,1433;Database=datawarehouse;Uid=allenj25;Pwd=Jack1998;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
# conn = pyodbc.PyODBCConnector()
# conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(db_url)
# engine = create_engine(conn_str)

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
