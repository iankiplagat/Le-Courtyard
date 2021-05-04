import os 

class Config(object):
  '''Config class'''
  
  SECRET_KEY = os.getenv('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
  CSRF_ENABLED = True
  
class DevConfig(Config):
  '''Development configuration'''
  
  DEBUG = True
  
  
class StageConfig(Config):
  '''Staging configuration'''
  
  DEBUG = True
  
  
class ProdConfig(Config):
  '''Production configuration'''
  
  DEBUG = False

  
class TestConfig(Config):
  '''Testing class configuration'''
  
  TESTING = True
  
  
app_config = {
  'development': DevConfig,
  'testing': TestConfig,
  'staging': StageConfig,
  'production': ProdConfig
}
  