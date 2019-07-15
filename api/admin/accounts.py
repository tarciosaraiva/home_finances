from flask_restplus import Namespace, Resource, fields
from pony.orm import db_session, commit

from api import account_model as account
from core.database import db

ns = Namespace('accounts')

@ns.route('/')
class AccountList(Resource):
    @ns.marshal_list_with(account)
    def get(self):
        '''List all accounts'''
        response = []
        accounts = db.Account.select().order_by(db.Account.name)

        for a in accounts:
            response.append(a)

        return response

    @db_session
    @ns.expect(account)
    @ns.marshal_with(account, code=201)
    def post(self):
        '''Create an account'''
        account_obj = db.Account(**ns.payload)
        commit
        return account_obj, 201


@ns.response(404, 'Account not found')
@ns.param('id', 'The Account identifier')
class AccountItem(Resource):
    @ns.marshal_with(account)
    def get(self, id):
        '''Get a single Account'''
        return db.Account[id]

    @db_session
    @ns.expect(account)
    @ns.marshal_with(account, code=204)
    def put(self, id):
        '''Update a single Account'''
        account = db.Account[id]
        account.set(**ns.payload)
        commit()
        return account, 204

    @db_session
    @ns.response(204, 'Account deleted')
    def delete(self, id):
        '''Delete a account'''
        db.Account[id].delete()