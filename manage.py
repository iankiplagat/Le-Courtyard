import os
from app import create_app,db
from flask_script import Manager,Server
from app.auth.v1.model.user_model import UserModels, Product
#from app.auth.v1.model.product_model import Product

config_name = os.getenv('APP_SETTINGS')

app = create_app(config_name)



manager = Manager(app)
manager.add_command('server',Server)
@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,UserModels = UserModels, Product=Product)


if __name__ == '__main__':
  manager.run()