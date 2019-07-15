from flask_restplus import Namespace, Resource, fields
from pony.orm import db_session, commit

from api import category_model as category
from core.database import db

ns = Namespace('categories')

@ns.route('/')
class CategoryList(Resource):
    @ns.marshal_list_with(category)
    def get(self):
        '''List all categories'''
        response = []
        categories = db.Category.select().order_by(db.Category.name)

        for c in categories:
            response.append(c)

        return response

    @db_session
    @ns.expect(category)
    @ns.marshal_with(category, code=201)
    def post(self):
        '''Create a category'''
        category_obj = db.Category(**ns.payload)
        commit()
        return category_obj, 201


@ns.response(404, 'Category not found')
@ns.param('id', 'The Category identifier')
class CategoryItem(Resource):
    @ns.marshal_with(category)
    def get(self, id):
        '''Get a single Category'''
        return db.Category[id]

    @db_session
    @ns.expect(category)
    @ns.marshal_with(category, code=204)
    def put(self, id):
        '''Update a single Category'''
        category = db.Category[id]
        category.set(**ns.payload)
        commit()
        return category, 204

    @db_session
    @ns.response(204, 'Category deleted')
    def delete(self, id):
        '''Delete a category'''
        db.Category[id].delete()