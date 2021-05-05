from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin






db = SQLAlchemy()
ma = Marshmallow()

class UserModels(UserMixin, db.Model):

  '''Class for user operation'''


  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(255), unique=True, index=True)
  pass_secure = db.Column(db.String(255))
   



  def save_user(self):
      db.session.add(self)
      db.session.commit()    

    

  def __repr__(self):
    return f'User {self.username}'   



class UserModelsSchema(ma.Schema):
  class Meta:
    fields = ('id','email','pass_secure')

User_schema = UserModelsSchema()
Users_schema = UserModelsSchema(many=True)


  # def register(self):
  #   '''method to sign up a user '''
  #   data = dict(
  #     userID = self.userId,
  #     email = self.email,
  #     password=self.password,
  #     confirm_password= self.confirm_password
  #   )
  #   self.users.append(data)
  #   return self.userId

  # def fetch_user_by_userId(self,userId):
  #   ''' Get a user instance using their id '''
  #   for user in users:
  #     if user['userId'] == userId:
  #       return user 
  
  # def fetch_all(self):
  #   '''Get the whole data'''
  #   return UserModels.users
