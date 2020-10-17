import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from database import models


DATABASE_URI = 'postgres+psycopg2://' + \
    os.environ['db_username'] + ':' + os.environ['db_password'] + \
    '@localhost:5432/' + os.environ['db_name']

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)


def initializeFromModels():
    models.Base.metadata.create_all(engine)

def clearDatabase():
    models.Base.metadata.drop_all(engine)

def recreate_database():
    models.Base.metadata.drop_all(engine)
