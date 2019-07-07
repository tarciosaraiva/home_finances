from flask_restplus import Namespace, Resource, fields

from core.database import Bucket

ns = Namespace('buckets', description='Operations for bucket')

@ns.route('/')
class Buckets(Resource):
    def get(self):
        '''List all buckets'''
        return Bucket.select()

    def post(self):
        '''Create a bucket'''
        return True
