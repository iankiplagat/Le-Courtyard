from flask import jsonify, make_response, request
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from app.auth.v1.utils.validator import Validators
from app.auth.v1.model.user_model import UserModels, UserModelsSchema, Users_schema, User_schema


validate = Validators()


def validate_username(username):
    user = UserModels.query.filter_by(username=username).first()
    return user


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
        if validate.valid_email(email):
            return validate.valid_email(email)
        if validate.user_exists(email, username):
            return validate.user_exists(email, username)

        newUser = UserModels(username=username, email=email, password=password)
        user = validate_username(username=username)

        newUser.save_user()
        result = User_schema.dump(newUser)

        return {
            "status": 201,
            "message": "User registered",
            "user": result
        }, 201


class Login(Resource):
    """class for user login"""

    def __init__(self):
        """Initialize the login class"""
        self.parser = RequestParser()
        self.parser.add_argument("username", type=str, required=True,
                                 help="please input a username")
        self.parser.add_argument("password", type=str, required=True,
                                 help="please input a password")

    def post(self):
        """method to login user"""
        data = self.parser.parse_args()
        data = request.get_json()
        username = data["username"]
        password = data["password"]

        user = UserModels.query.filter_by(username=username).first()
        if validate.validate_user(username):
            return validate.validate_user(username)
        if user.verify_password(password) is not True:
            return {
                "status": 404,
                "error": "Wrong password"
            }, 401

        return {
            "status": 200,
            "message": "Logged in as {}".format(username),
            "data": User_schema.dump(user)
        }, 200
