import jwt
import pyotp
from config import SECRET_KEY
from flask_restful import request, Resource
from db import db_connection

class ActivateOTPHandler(Resource):
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
    
    data = request.json
    idno = request.args.get('id')
    isActivated = data.get('isactivated')            
    conn = db_connection() 
    cursor = conn.cursor() 

    users=cursor.execute("SELECT * FROM users WHERE id = %s", idno)
    result = cursor.fetchone()
    if (users):
      TOTPSECRETKEY = result['secretkey']
      if (isActivated == 'Y'):    
          fullname = result['firstname'] + ' ' + result['lastname']
          qrcode = pyotp.totp.TOTP(TOTPSECRETKEY).provisioning_uri(name=fullname, issuer_name="DOHA BANK")
          cursor.execute("UPDATE users SET qrcodeurl = %s WHERE id = %s",(qrcode, idno))   
          conn.commit()
          return { 'statuscode': 200, 'message': 'Activated.', 'qrcodeurl': qrcode }
      else:
          sql = """UPDATE users SET qrcodeurl = %s WHERE id = %s"""
          cursor.execute(sql, (None, idno))
          conn.commit()
      return { 'statuscode': 200, 'message': 'De-Activated.' }
       
