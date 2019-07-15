from flask_restplus import Namespace, Resource, fields
from pony.orm import db_session, commit

from api import item_model as item
from core.database import db

ns = Namespace('item')

@ns.route('/')
@ns.param('budget_id', 'The Budget identifier')
class BudgetItemList(Resource):
    @ns.marshal_list_with(item)
    def get(self, budget_id):
        '''List all items'''
        response = []
        items = db.Item.select().order_by(db.Item.name)

        for a in items:
            response.append(a)

        return response

    @db_session
    @ns.expect(item)
    @ns.marshal_with(item, code=201)
    def post(self, budget_id):
        '''Create an item'''
        item_obj = db.Item(**ns.payload)
        commit()
        return item_obj, 201


@ns.response(404, 'Item not found')
@ns.param('budget_id', 'The Budget identifier')
@ns.param('id', 'The Item identifier')
class BudgetItemItem(Resource):
    @ns.marshal_with(item)
    def get(self, budget_id, id):
        '''Get a single Item'''
        return db.Item[id]

    @db_session
    @ns.response(204, 'Item deleted')
    def delete(self, budget_id, id):
        '''Delete a item'''
        db.Item[id].delete()
