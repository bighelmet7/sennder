from flask import Blueprint
from flask_restful import Api

from v1.resources.movies import MoviesResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Movies Endpoint
api.add_resource(MoviesResource, '/v1/movies/')
