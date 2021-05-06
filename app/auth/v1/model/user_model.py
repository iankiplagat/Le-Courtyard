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

class Product(db.Model):
  __tablename__ = 'products'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(100), unique = True)
  description = db.Column(db.String(200))
  price = db.Column(db.Float)
  qty = db.Column(db.Integer)
  
  #def __init__(self, name, description, price, qty):
    #self.name = name
    #self.description = description
    #self.price = price
    #self.qty = qty

  def save_product(self):
    db.session.add(self)
    db.session.commit()

  def get_product(self):
    db.session.commit()

  
   

#Product Schema
class ProductSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'description', 'price', 'qty')


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)









  
