from flask_restful import Resource,request

class DeleteuserHandler(Resource):

  def delete(self):
    idno = request.args.get('id')

    return {
      'statuscode': 200,
      'resultStatus': 'SUCCESS',
      'userid': idno,
      'message': 'Delete User ID...'
      }, 200
      
