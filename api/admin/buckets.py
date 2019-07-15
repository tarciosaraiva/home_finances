from flask_restplus import Namespace, Resource, fields
from pony.orm import db_session, commit

from api import bucket_model as bucket
from core.database import db

ns = Namespace('buckets')

@ns.route('/')
class BucketList(Resource):
    @ns.marshal_list_with(bucket)
    def get(self):
        '''List all buckets'''
        response = []
        buckets = db.Bucket.select().order_by(db.Bucket.name)

        for b in buckets:
            response.append(b)

        return response

    @db_session
    @ns.expect(bucket)
    @ns.marshal_with(bucket, code=201)
    def post(self):
        '''Create a bucket'''
        bucket_obj = db.Bucket(**ns.payload)
        commit()
        return bucket_obj, 201


@ns.response(404, 'Bucket not found')
@ns.param('id', 'The Bucket identifier')
class BucketItem(Resource):
    @ns.marshal_with(bucket)
    def get(self, id):
        '''Get a single Bucket'''
        return db.Bucket[id]

    @db_session
    @ns.expect(bucket)
    @ns.marshal_with(bucket, code=204)
    def put(self, id):
        '''Update a single Bucket'''
        bucket = db.Bucket[id]
        bucket.set(**ns.payload)
        commit()
        return bucket, 204

    @db_session
    @ns.response(204, 'Bucket deleted')
    def delete(self, id):
        '''Delete a bucket'''
        db.Bucket[id].delete()