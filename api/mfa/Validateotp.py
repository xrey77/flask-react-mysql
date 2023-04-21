import pyotp
import time
from flask_restful import request, Resource
from db import db_connection

class ValidateOTPHandler(Resource):
  def post(self):
    data = request.json
    idno = data.get('id')
    otp = data.get('otpcode')
    try:
        conn = db_connection() 
        cursor = conn.cursor() 
        users=cursor.execute("SELECT * FROM users WHERE id = %s", idno)
        result = cursor.fetchone()
        TOTPSECRET = result['secretkey']
        if (users):
        # if pyotp.TOTP(secret,interval=60).verify(otp):

            token = pyotp.TOTP(TOTPSECRET)
            isOk = token.verify(otp)
            if isOk:
                return { 'statuscode': 200, 'message': 'OTP Code is valid.','username': result['username'] }
            else:
                return { 'statuscode': 404, 'message': 'Invalid OTP Code, please try again. 1' }
    except Exception as e:
            return { 'statuscode': 404, 'message': 'Invalid OTP Code, please try again. 2' }           
              
