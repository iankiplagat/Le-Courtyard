from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .auth.v1 import version1 as v1
from instance.config import app_config
from .auth.v1.model.user_model import db,ma

#from .auth.v1.model.product_model import db, ma



def create_app(config_name):
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_object(app_config[config_name])
  app.config.from_pyfile('config.py')
  app.url_map.strict_slashes = False
  db.init_app(app)
  ma.init_app(app)
  
  from .product import product as product_blueprint
  app.register_blueprint(v1)
  app.register_blueprint(product_blueprint)

  return app
