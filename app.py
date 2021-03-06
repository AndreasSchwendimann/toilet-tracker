from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.Session import SessionResource
from resources.Event import EventResource


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes

api.add_resource(Hello, '/Hello')
api.add_resource(SessionResource, '/Session')
api.add_resource(EventResource, '/Event')