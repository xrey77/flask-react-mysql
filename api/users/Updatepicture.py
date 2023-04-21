from flask_restful import request, Resource
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from db import db_connection

UPLOAD_FOLDER = 'assets/users/'

class UpdatepictureHandler(Resource):

  def post(self):
   if request.method == 'POST':
    idno = request.args.get('id')
    ext = request.form.get('ext')
    f = request.files['file']
    newfile = "00" + idno + ext
    f.save(UPLOAD_FOLDER + secure_filename(newfile))
    urlfile = "http://127.0.0.1:5000/assets/users/"+ newfile
    conn = db_connection() 
    cursor = conn.cursor()        
    cursor.execute("UPDATE users SET picture = %s WHERE id = %s",(urlfile, idno))   
    conn.commit()
    return { 'statuscode': 200, 'message': 'ok', 'id': idno}