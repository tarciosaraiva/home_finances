from flask_restplus import Namespace, Resource, fields
from pony.orm import db_session, commit

from api import budget_model as budget
from core.database import db

ns = Namespace('budget')

@ns.route('/')
class BudgetList(Resource):
    @ns.marshal_list_with(budget)
    def get(self):
        '''List all budgets'''
        response = []
        budgets = db.Budget.select().order_by(db.Budget.name)

        for a in budgets:
            response.append(a)

        return response

    @db_session
    @ns.expect(budget)
    @ns.marshal_with(budget, code=201)
    def post(self):
        '''Create an budget'''
        budget_obj = db.Budget(**ns.payload)
        commit()
        return budget_obj, 201


@ns.response(404, 'Budget not found')
@ns.param('id', 'The Budget identifier')
class BudgetItem(Resource):
    @ns.marshal_with(budget)
    def get(self, id):
        '''Get a single Budget'''
        return db.Budget[id]

    @db_session
    @ns.response(204, 'Budget deleted')
    def delete(self, id):
        '''Delete a budget'''
        db.Budget[id].delete()