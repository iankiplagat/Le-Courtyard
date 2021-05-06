from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()

class Product(db.Model):
  __tablename__ = 'products'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(100), unique = True)
  description = db.Column(db.String(200))
  price = db.Column(db.Float)
  qty = db.Column(db.Integer)
  
  def __init__(self, name, description, price, qty):
    self.name = name
    self.description = description
    self.price = price
    self.qty = qty

  def save_product(self):
    db.session.add(self)
    db.session.commit()

#Product Schema
class ProductSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'description', 'price', 'qty')


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

