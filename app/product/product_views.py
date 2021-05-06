from flask import jsonify,make_response,request, Flask
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from app.auth.v1.model.user_model import Product, ProductSchema, product_schema, products_schema
from . import product
from app import db



#class Products(Resource):
  #'''Class to register product(s)'''

@product.route('/product', methods = ['POST'])
def add_product():
  name = request.json['name']
  description = request.json['description']
  price = request.json['price']
  qty = request.json['qty']
  
  new_product = Product(name = name, description = description, price = price, qty = qty)
  
  new_product.save_product()

  return product_schema.jsonify(new_product)

#Get Single Product
@product.route('/product/<id>', methods = ['GET'])
def get_product(id):
  product = Product.query.get(id)
  
  return product_schema.jsonify(product)

#Get All Products
@product.route('/product', methods = ['GET'])
def get_products():
  all_products = Product.query.all()
  result = products_schema.dump(all_products)
  
  return jsonify(result)

#Update a product
@product.route('/product/<id>', methods = ['PUT'])
def update_product(id):
  product = Product.query.get(id)
  
  name = request.json['name']
  description = request.json['description']
  price = request.json['price']
  qty = request.json['qty']
  product.name = name
  product.description = description
  product.price = price
  product.qty = qty
 
  product.get_product()
  
  return product_schema.jsonify(product)

#Delete a Product by Id
@product.route('/product/<id>', methods = ['DELETE'])
def delete_product(id):
  product = Product.query.get(id)
  
  db.session.delete(product)
  db.session.commit()
  
  return product_schema.jsonify(product)















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



