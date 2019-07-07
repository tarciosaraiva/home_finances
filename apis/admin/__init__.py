from flask import Blueprint
from flask_restplus import Api, Resource, fields

from .categories import ns as category_ns
from .buckets import ns as bucket_ns

blueprint = Blueprint('admin', __name__)
api = Api(blueprint)

ns = api.namespace('admin', description='Admin operations for Category')

api.add_namespace(category_ns, '/categories')
api.add_namespace(bucket_ns, '/buckets')