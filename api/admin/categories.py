from flask_restplus import Namespace, Resource, fields

from core.database import Category

ns = Namespace('categories')

@ns.route('/')
class Categories(Resource):
    def get(self):
        '''List all categories'''
        return Category.select()

    def post(self):
        '''Create a category'''
        return True
