from sqlalchemy.engine import url, create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy

db_url = url.URL(
    drivername='ODBC Driver 13 for SQL Server',
    username='allenj25',
    password='Jack1998',
    host='css439.database.windows.net',
    port='1433',
    database='datawarehouse',
)
test= "please for the love of god work"
engine = create_engine(db_url)

Session = sessionmaker(bind = engine)

session = Session()
