from flask_restplus import Namespace

from .budgets import BudgetItem, BudgetList
from .budget_items import BudgetItemItem, BudgetItemList

ns = Namespace('budgets', description='Budget operations')

ns.add_resource(BudgetItem, '/<int:id>')
ns.add_resource(BudgetList, '/')

ns.add_resource(BudgetItemItem, '/<int:budget_id>/items/<int:id>')
ns.add_resource(BudgetItemList, '/<int:budget_id>/items')
