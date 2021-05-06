from flask import jsonify,make_response,request
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from app.auth.v1.model.product_model import Product, ProductSchema, product_schema, products_schema
from . import product
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()


class Products(Resource):
  '''Class to register product(s)'''

  @product.route('/product', methods = ['POST'])
  def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']
    
    new_product = Product(name,description,price,qty)
    
    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)















#   def __init__(self):
#     self.parser = RequestParser()
#     self.parser.add_argument('name', type=str, required=True,
#                             help="please input your name")
#     self.parser.add_argument("description", type=str, required=True,
#                             help="description")
#     self.parser.add_argument("price", type=str, required=True,
#                             help="price")
#     self.parser.add_argument("qty", type=str, required=True,
#                             help="Enter quantity")
                  
# def post(self):
#     '''Register product endpoint'''
#     args = self.parser.parse_args()
#     args = request.get_json()

#     name = args["name"]
#     description = args["description"]
#     price = args["price"]
#     qty = args["qty"]


    # newProduct = Product(name=name, description=description, price=price, qty=qty)
    # newProduct.save_product()
    # result = Product_schema.dump(newProduct)



    # return {
    # "status": 201,
    # "message": "product registered",
    # "product": jsonify(result)
    # }, 201



