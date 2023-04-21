import jwt
from config import SECRET_KEY
from flask_restful import request, Resource
from db import db_connection
from flask_bcrypt import generate_password_hash

class UpdateuserHandler(Resource):
  def put(self):
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
    data = request.json

    fname = data.get("firstname")
    lname = data.get("lastname")
    mobile = data.get("mobileno")
    pwd = data.get('password')
    hashpwd = generate_password_hash(pwd,10)

    conn = db_connection() 
    cursor = conn.cursor()
    if pwd == None:
      cursor.execute("UPDATE users SET lastname = %s, firstname = %s, mobileno = %s WHERE id = %s",(lname, fname, mobile, idno))   
      conn.commit()
    else:
      cursor.execute("UPDATE users SET lastname = %s, firstname = %s, mobileno = %s, password = %s WHERE id = %s",(lname, fname, mobile, hashpwd, idno))   
      conn.commit()
      
    return { 'statuscode': 200, 'message': 'Profile updated.' }