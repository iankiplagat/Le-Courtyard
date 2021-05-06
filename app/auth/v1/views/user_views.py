from flask import jsonify,make_response,request
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from app.auth.v1.model.user_model import UserModels,UserModelsSchema,Users_schema,User_schema

class Users(Resource):
  '''Class to register user(s)'''

  def __init__(self):
    self.parser = RequestParser()
    self.parser.add_argument('username', type=str, required=True,
                            help="please input a username")
    self.parser.add_argument('email', type=str, required=True,
                            help="please input an email")
    self.parser.add_argument("password", type=str, required=True,
                            help="please input a password")


  
  
  def post(self):
    '''Register user endpoint'''
    args = self.parser.parse_args()
    args = request.get_json()
    username = args["username"]
    email = args["email"]
    password = args["password"]


    newUser = UserModels(username=username,email=email, password=password)
    newUser.save_user()
    result = User_schema.dump(newUser)
    


    return {
      "status": 201,
      "message": "User registered",
      "user": result
    }, 201



  
