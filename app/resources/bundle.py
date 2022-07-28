from flask_restful import Resource, reqparse
from app.models.bundle import BundleModel
from app.decorators import auth_required


# class controlling bundle resource
class Bundle(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title')
    parser.add_argument('level')
    parser.add_argument('description')
    parser.add_argument('outline')

    @auth_required(3)
    def post(user, self, id):
        data = Bundle.parser.parse_args()
        try:
            bundle = BundleModel(
                title=data['title'],
                level=data['level'],
                description=data['description'],
                outline=data['outline']
            )
            bundle.save_to_db()
        except Exception:
            return {'message': 'Error with bundle creation'}, 404
        return bundle.json(), 201

    @auth_required(1)
    def get(user, self, id):
        bundle = BundleModel.find_by_id(int(id))
        if bundle:
            return bundle.json()
        return {'message': 'Bundle not found'}, 404

    @auth_required(3)
    def put(user, self, id):
        data = Bundle.parser.parse_args()
        bundle = BundleModel.find_by_id(int(id))
        if bundle:
            bundle.update(**data)
        else:
            {'message': 'Bundle not found'}, 404
        bundle.save_to_db()
        return bundle.json()

    @auth_required(3)
    def delete(user, self, id):
        bundle = BundleModel.find_by_id(int(id))
        if bundle:
            bundle.delete_from_db()
            return {'message': 'Bundle deleted.'}
        return {'message': 'Bundle not found.'}, 404


# class controlling bundle resource
class BundleList(Resource):
    def get(self):
        return {'items': list(map(lambda x: x.summary(),
                                  BundleModel.query.all()))}


# class controlling bundle resource
class BundleListAdmin(Resource):
    @auth_required(3)
    def get(user, self):
        return {'items': list(map(lambda x: x.summary(),
                                  BundleModel.query.all()))}
