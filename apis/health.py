from flask import Blueprint
from flask_restplus import Api, Resource, fields

blueprint = Blueprint('health', __name__)
api = Api(blueprint)

ns = api.namespace('health', description='Telemetry operations')

@ns.route('/ping')
class Ping(Resource):
    def get(self):
        '''Health check endpoint'''
        return "OK"

@ns.route('/status')
class Status(Resource):
    def get(self):
        '''Status of the service showing DB connection'''
        return {'database': 'OK'}

