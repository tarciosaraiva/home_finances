from flask_restplus import Namespace

from .budgets import BudgetItem, BudgetList
# from .items import ItemsItem, ItemsList

ns = Namespace('budget', description='Budget operations')

ns.add_resource(BudgetItem, '/<int:id>')
ns.add_resource(BudgetList, '/')

# ns.add_resource(AccountItem, '/account/<int:id>')
# ns.add_resource(AccountList, '/accounts')
