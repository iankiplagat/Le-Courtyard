from flask import jsonify,make_response,request
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from app.auth.v1.model.user_model import UserModels

class Users(Resource):
  '''Class to register user(s)'''

  def __init__(self):
    self.parser = RequestParser()
    self.parser.add_argument('email', type=str, required=True,
                            help="please input an email")
    self.parser.add_argument("password", type=str, required=True,
                            help="please input a password")
    self.parser.add_argument("confirm_password", type=str, required=True,
                            help="kindly confirm your password")

  def get(self):
    '''Get all user endpoint'''
    users = UserModels.fetch_all(self)
    return {
      "users": users
    }
  
  
  def post(self):
    '''Register use endpoint'''
    args = self.parser.parse_args()
    args = request.get_json()

    email = args["email"]
    password = args["password"]
    confirm_password = args["confirm_password"]

    newUser = UserModels(email, password, confirm_password)
    newUser.register()

    return {
      "status": 201,
      "message": "User registered",
      "user": newUser.__dict__
    }, 201



  
