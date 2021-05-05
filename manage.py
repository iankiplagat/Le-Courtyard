import os
from app import create_app,db
from flask_script import Manager,Server
from app.auth.v1.model.user_model import UserModels

config_name = os.getenv('APP_SETTINGS')

app = create_app(config_name)



manager = Manager(app)
manager.add_command('server',Server)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,UserModels = UserModels )

if __name__ == '__main__':
  manager.run()