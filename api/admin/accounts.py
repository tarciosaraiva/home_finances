from flask_restplus import Namespace, Resource, fields

from core.database import Account

ns = Namespace('accounts')

@ns.route('/')
class Accounts(Resource):
    def get(self):
        '''List all accounts'''
        return Bucket.select()

    def post(self):
        '''Create an account'''
        return True
