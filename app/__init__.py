from flask import Flask
from .auth.v1 import version1 as v1

from instance.config import app_config

def create_app(config_name):
  app = Flask(__name__, instance_relative_config=True)
  
  app.config.from_object(app_config[config_name])
  ##############
  app.url_map.strict_slashes = False
  
  
  return app