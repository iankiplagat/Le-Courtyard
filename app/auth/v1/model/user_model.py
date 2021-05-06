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
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def fetch_all_users(self):
        users = UserModels.query.all()
        return users

    def __repr__(self):
        return f'User {self.username}'


class UserModelsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'pass_secure')


User_schema = UserModelsSchema()
Users_schema = UserModelsSchema(many=True)

