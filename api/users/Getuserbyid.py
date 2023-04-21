import jwt
from config import SECRET_KEY
from flask_restful import request, Resource
from db import db_connection


class GetuserbyidHandler(Resource):

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

    idno = request.args.get('id')    
    conn = db_connection()
    cursor = conn.cursor()
    users=cursor.execute("SELECT * FROM users WHERE id = %s", idno)
    result = cursor.fetchone()
    if (users):
        return { 'statuscode': 200, 'message': 'User data has been retrieved.', 'user': result}

    return {
      'statuscode': 404,
      'message': 'No records found.'
      }, 200
      
      
