### config.py ###
# pip install flask-jsontools

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
# from flask.ext.jsontools import JsonSerializableBase

# Base = declarative_base(cls=(JsonSerializableBase,))

DATABASE_URI='mysql://rey:rey@127.0.0.1/flask_react_mysql'
SECRET_KEY = 'cluxzT2pcP0OVP0w1qmri9Es9wX4n6N6q3LIjyN9t6w='

Base = declarative_base()
engine = create_engine(DATABASE_URI)
db_session = scoped_session(sessionmaker(autocommit=True,
                                         autoflush=True,
                                         bind=engine))
def init_db():
    Base.metadata.create_all(engine)


