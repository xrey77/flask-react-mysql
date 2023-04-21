import jwt
from flask import current_app

from flask_restful import request, Resource
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError
from sqlalchemy import create_engine
from flask_bcrypt import generate_password_hash
from db import db_connection
from config import SECRET_KEY

class GetusersHandler(Resource):

  def get(self):
    try:
      headers = request.headers
      bearer = headers.get('Authorization')
      token = bearer.split()[1] 
      jwt.decode(token, SECRET_KEY, algorithms=["HS256"])    
    except Exception as e:
      return {
        'statuscode': 401,
        'token': 'UnAuthorized Access.'
        }, 401
    
    conn = db_connection()
    cursor = conn.cursor()
    sql = """SELECT * FROM users"""
    users=cursor.execute(sql)
    results = cursor.fetchall()
    if (users):
        return results

    return {
      'statuscode': 404,
      'message': 'No records found.'
      }, 404
      
