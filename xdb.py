from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

def db():
    try:
        engine = create_engine("mysql://rey:rey@127.0.0.1/flask_react_mysql")
    except SQLAlchemyError as err:
        print("error", err.__cause__)         
        return {'Error': err.__cause__}
    print("connected...")
    return engine.connect()
