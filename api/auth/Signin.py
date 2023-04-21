from flask_restful import request, Resource
import jwt
from db import db_connection
from flask_bcrypt import check_password_hash
import datetime
from config import SECRET_KEY

class SigninHandler(Resource):

  def post(self):
    conn = db_connection()
    cursor = conn.cursor()

    data = request.json
    usrname = data.get('username')
    pwd = data.get('password')

    sql1 = """SELECT * FROM users WHERE username = %s"""
    key1=[(usrname)]
    usr=cursor.execute(sql1,key1)
    rec = cursor.fetchall()
    if (usr):
          hashpwd = rec[0]['password']
          if (check_password_hash(hashpwd,pwd)):
            fullname = rec[0]['email']
            token=encode_auth_token(fullname)
            return {
               'statuscode': 200,
               'message': 'ok',
               'userid': rec[0]['id'],
               'username': rec[0]['username'],
               'picture': rec[0]['picture'],
               'isactivated': rec[0]['isactivated'],
               'isblocked': rec[0]['isblocked'],
               'qrcodeurl': rec[0]['qrcodeurl'],
               'token': token}, 200
          else:             
            return {'statuscode': 404,'message': 'Invalid Password, try again.'}, 404
    
    return {
      'statuscode': 404,
      'message': "Username not found."
      }, 404
      
def encode_auth_token(user):
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': user
        }
        return jwt.encode(
            payload,
            SECRET_KEY,
            algorithm='HS256'
        )
    except Exception as e:
        return e

