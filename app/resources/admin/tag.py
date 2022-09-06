from flask_restful import Resource, reqparse
from app.models.tag import TagModel
from flask import Response, json
from app.decorators import auth_required


class AdminTag(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('tag', type=str)

    @auth_required(3)
    def get(user, self, id):
        raw = TagModel.find_by_id(int(id))
        if raw:
            return raw.json()
        return {'message': 'raw not found'}, 404

    @auth_required(3)
    def put(user, self, id):
        data = AdminTag.parser.parse_args()
        raw = TagModel.find_by_id(int(id))
        if raw:
            raw.update(**data)
        else:
            {'message': 'raw not found'}, 404
        raw.save_to_db()
        return raw.json()

    @auth_required(3)
    def delete(user, self, id):
        raw = TagModel.find_by_id(int(id))
        if raw:
            raw.delete_from_db()
            return {'message': 'raw deleted.'}
        return {'message': 'raw not found.'}, 404


class AdminTagList(Resource):
    @auth_required(3)
    def get(user, self):
        data = list(map(lambda x: x.json(), TagModel.query.all()))
        response = Response(json.dumps(data))
        response.headers['Content-Range'] = len(data)
        return response

    @auth_required(3)
    def post(user, self):
        data = AdminTag.parser.parse_args()
        try:
            raw = TagModel(**data)
            raw.save_to_db()
        except Exception:
            return {'message': 'Error with raw creation'}, 404
        return raw.json(), 201
