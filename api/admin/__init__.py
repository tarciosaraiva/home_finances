from flask_restplus import Namespace

from .buckets import BucketItem, BucketList
from .accounts import AccountItem, AccountList
from .categories import CategoryItem, CategoryList

ns = Namespace('admin', description='Admin operations for Category')

ns.add_resource(BucketItem, '/bucket/<int:id>')
ns.add_resource(BucketList, '/buckets')

ns.add_resource(AccountItem, '/account/<int:id>')
ns.add_resource(AccountList, '/accounts')

ns.add_resource(CategoryItem, '/category/<int:id>')
ns.add_resource(CategoryList, '/categories')