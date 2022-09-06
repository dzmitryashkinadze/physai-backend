from flask_restful import Resource, reqparse
from app.models.user_login import UserLoginModel
from flask import Response, json
from app.decorators import auth_required


class AdminUserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('user_id', type=int)

    @auth_required(3)
    def get(user, self, id):
        raw = UserLoginModel.find_by_id(int(id))
        if raw:
            return raw.json()
        return {'message': 'raw not found'}, 404

    @auth_required(3)
    def put(user, self, id):
        data = AdminUserLogin.parser.parse_args()
        raw = UserLoginModel.find_by_id(int(id))
        if raw:
            raw.update(**data)
        else:
            {'message': 'raw not found'}, 404
        raw.save_to_db()
        return raw.json()

    @auth_required(3)
    def delete(user, self, id):
        raw = UserLoginModel.find_by_id(int(id))
        if raw:
            raw.delete_from_db()
            return {'message': 'raw deleted.'}
        return {'message': 'raw not found.'}, 404


class AdminUserLoginList(Resource):
    @auth_required(3)
    def get(user, self):
        data = list(map(lambda x: x.json(), UserLoginModel.query.all()))
        response = Response(json.dumps(data))
        response.headers['Content-Range'] = len(data)
        return response

    @auth_required(3)
    def post(user, self):
        data = AdminUserLogin.parser.parse_args()
        try:
            raw = UserLoginModel(**data)
            raw.save_to_db()
        except Exception:
            return {'message': 'Error with raw creation'}, 404
        return raw.json(), 201
