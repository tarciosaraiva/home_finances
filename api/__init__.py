from flask import Blueprint
from flask_restplus import Api, fields

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint)

bucket_model = api.model('bucket', {
    'id': fields.Integer(required=True),
    'name': fields.String(required=True),
    'threshold': fields.Float(required=False),
})

# importing namespace have to come after
# since model is defined at API level
# and used in the resources

from .admin import ns as admin_ns
from .health import ns as health_ns

api.add_namespace(admin_ns, '/admin')
api.add_namespace(health_ns, '/health')