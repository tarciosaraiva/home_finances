from flask_restplus import Namespace, Resource, fields

from core.database import db

ns = Namespace('status')

@ns.route('/')
class Status(Resource):
    def get(self):
        '''Status of the service showing DB connection'''
        db_status = 'OK' if len(db.select('SELECT 1')) == 1 else 'NOK'
        return {'database': db_status}

