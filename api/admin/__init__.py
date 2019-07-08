from flask_restplus import Namespace

from .buckets import BucketItem, BucketList
from .accounts import Accounts
from .categories import Categories

ns = Namespace('admin', description='Admin operations for Category')

ns.add_resource(BucketItem, '/bucket/<int:id>')
ns.add_resource(BucketList, '/buckets')

ns.add_resource(Accounts, '/accounts')
ns.add_resource(Categories, '/categories')