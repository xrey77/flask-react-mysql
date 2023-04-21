import pymysql
import pyotp
from flask_restful import request, Resource
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError
from sqlalchemy import create_engine
from flask_bcrypt import generate_password_hash
from db import db_connection

class SignupHandler(Resource):

  def post(self):
    conn = db_connection()
    cursor = conn.cursor()

    data = request.json
    fname = data.get('firstname')
    lname = data.get('lastname')
    email = data.get('email')
    mobile = data.get('mobileno')
    usrname = data.get('username')
    pwd = data.get('password')
    hashpwd = generate_password_hash(pwd,10)

    # CHECK EMAIL ADDRESS
    sql1 = """SELECT * FROM users WHERE email = %s"""
    key1=[(email)]
    find_email=cursor.execute(sql1,key1)
    if (find_email):
        return {
            'message': 'Email Address has been taken.'
        }
    
    # GENERATE TOTP SECRET KEY
    secret = pyotp.random_base32()

    # CHECK USERNAME
    sql2 = """SELECT * FROM users WHERE username = %s"""
    key2=[(usrname)]
    find_username=cursor.execute(sql2,key2)
    if (find_username):
        return {
            'message': 'Username has been taken.'
        }

    # INSERT INPUT JSON DATA
    try:
      useric = "http://127.0.0.1:5000/assets/users/user.jpg"
      sql3="""INSERT INTO users(lastname,firstname,email,mobileno,username,password,picture,secretkey) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"""
      cursor.execute(sql3, (lname, fname, email, mobile, usrname, hashpwd, useric, secret))
      conn.commit()
    except pymysql.Error as e:
      return {
        'statuscode': 500,
        'message': e.args
        }      
    finally:
      return {
        'statuscode': 200,
        'resultStatus': 'SUCCESS',
        'message': "Signup successfull..."
        }