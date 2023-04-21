import datetime
from flask import Flask, redirect, url_for, request, send_from_directory
from flask_restful import Resource, Api
from flask_cors import CORS #comment this on deployment
from api.auth.Signin import SigninHandler
from api.auth.Signup import SignupHandler
from api.users.Getusers import GetusersHandler
from api.users.Getuserbyid import GetuserbyidHandler
from api.users.Updateuser import UpdateuserHandler
from api.users.Deleteuser import DeleteuserHandler
from api.users.Updatepicture import UpdatepictureHandler
from api.mfa.Activatetop import ActivateOTPHandler
from api.mfa.Validateotp import ValidateOTPHandler
from api.products.Getproducts import GetproductsHandler
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow

app = Flask(__name__, static_url_path='', static_folder='clientapp/build')

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://rey:rey@127.0.0.1/flask_react_mysql'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# ma = Marshmallow(db)

CORS(app) #comment this on deployment
# app = Flask(__name__, upload_folder='assets') 

api = Api(app)

# ASSETS STATIC FOLDER
@app.route('/assets/<path:path>')
def assets_folder(path):
    return send_from_directory('assets', path)

# CALL REACTJS clientapp/build folder
@app.route("/", defaults={'path':''})

def serve(path: any):
    return send_from_directory(app.static_folder,'index.html')





# CALL API
api.add_resource(SigninHandler, '/api/signin')
api.add_resource(SignupHandler, '/api/signup')
api.add_resource(GetusersHandler, '/api/getallusers')
api.add_resource(GetuserbyidHandler, '/api/getuserbydi')
api.add_resource(UpdateuserHandler, '/api/updateuser')
api.add_resource(DeleteuserHandler, '/api/deleteuser')
api.add_resource(ActivateOTPHandler, '/api/activateotp')
api.add_resource(UpdatepictureHandler, '/api/updateuserpicture')
api.add_resource(ValidateOTPHandler, '/api/validateotpcode')
api.add_resource(GetproductsHandler, '/api/getallproducts')

if __name__ == "__main__":
    app.run()
    # app.run(debug=False, host='0.0.0.0')
