from sqlalchemy.engine import url, create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy
import yaml

db_url = url.URL(
    drivername='py',
    username='',
    password='',
    host='127.0.0.1',
    port='3306',
    database='',
)

engine = create_engine(db_url)

Session = sessionmaker(bind = engine)

session = Session()
