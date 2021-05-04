from flask import Blueprint
from flask_restful import Api

version1 = Blueprint('auth_v1', __name__, url_prefix='/api/v1')

app = Api(version1, catch_all_404s = True)