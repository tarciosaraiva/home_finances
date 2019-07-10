from flask import Blueprint
from flask_restplus import Api, fields

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint)

bucket_model = api.model('bucket', {
    'id': fields.Integer(required=True),
    'name': fields.String(required=True),
    'threshold': fields.Float(required=False),
})

account_model = api.model('account', {
    'id': fields.Integer(required=True),
    'name': fields.String(required=True),
    'number': fields.String(required=False),
    'branch': fields.String(required=False),
})

category_model = api.model('category', {
    'id': fields.Integer(required=True),
    'name': fields.String(required=True),
})

item_model = api.model('item', {
    'id': fields.Integer(required=True),
    'description': fields.String(required=True),
    'category': fields.Nested(category_model, required=True),
    'bucket': fields.Nested(bucket_model, required=True),
    'type': fields.String(required=True),
    'frequency': fields.String(required=True),
    'amount': fields.Float(required=True),
})

budget_model = api.model('budget', {
    'id': fields.Integer(required=True),
    'user': fields.String(required=True),
    'items': fields.List(fields.Nested(item_model)),
    'name': fields.String(required=True),
    'preferred': fields.Boolean(required=True, default=False),
    'created_at': fields.DateTime(dt_format='iso8601', required=True),
})

# importing namespace have to come after
# since model is defined at API level
# and used in the resources

from .admin import ns as admin_ns
from .budget import ns as budget_ns
from .health import ns as health_ns

api.add_namespace(health_ns, '/health')
api.add_namespace(budget_ns, '/budget')
api.add_namespace(admin_ns, '/admin')
