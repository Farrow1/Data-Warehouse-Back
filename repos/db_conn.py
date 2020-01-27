from sqlalchemy.engine import url, create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy
import yaml

# with open(r'..\config.yaml') as config_args:
#     db_args = yaml.load(config_args, Loader=yaml.FullLoader)



# db_url = url.URL(
#     drivername = db_args.drivername,
#     username=  db_args.username,
#     password = db_args.password,
#     host = db_args.host,
#     port = db_args.port,
#     database = db_args.database,
# )

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
