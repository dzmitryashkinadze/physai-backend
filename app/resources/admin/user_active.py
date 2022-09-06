from flask_restful import Resource, reqparse
from app.models.user_active import UserActiveModel
from flask import Response, json
from app.decorators import auth_required


class AdminUserActive(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('user_id', type=int)
    parser.add_argument('frame_id', type=int)
    parser.add_argument('lesson_id', type=int)
    parser.add_argument('course_id', type=int)

    @auth_required(3)
    def get(user, self, id):
        raw = UserActiveModel.find_by_id(int(id))
        if raw:
            return raw.json()
        return {'message': 'raw not found'}, 404

    @auth_required(3)
    def put(user, self, id):
        data = AdminUserActive.parser.parse_args()
        raw = UserActiveModel.find_by_id(int(id))
        if raw:
            raw.update(**data)
        else:
            {'message': 'raw not found'}, 404
        raw.save_to_db()
        return raw.json()

    @auth_required(3)
    def delete(user, self, id):
        raw = UserActiveModel.find_by_id(int(id))
        if raw:
            raw.delete_from_db()
            return {'message': 'raw deleted.'}
        return {'message': 'raw not found.'}, 404


class AdminUserActiveList(Resource):
    @auth_required(3)
    def get(user, self):
        data = list(map(lambda x: x.json(), UserActiveModel.query.all()))
        response = Response(json.dumps(data))
        response.headers['Content-Range'] = len(data)
        return response

    @auth_required(3)
    def post(user, self):
        data = AdminUserActive.parser.parse_args()
        try:
            raw = UserActiveModel(**data)
            raw.save_to_db()
        except Exception:
            return {'message': 'Error with raw creation'}, 404
        return raw.json(), 201
