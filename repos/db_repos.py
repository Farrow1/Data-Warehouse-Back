from db_conn import session
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base

def default():
    return None

