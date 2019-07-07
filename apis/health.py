from flask import Blueprint
from flask_restplus import Api, Resource, fields

from core.database import db

blueprint = Blueprint('health', __name__)
api = Api(blueprint)

ns = api.namespace('health', description='Telemetry operations')

@ns.route('/status')
class Status(Resource):
    def get(self):
        '''Status of the service showing DB connection'''
        db_status = 'OK' if len(db.select('SELECT 1')) == 1 else 'NOK'
        return {'database': db_status}

