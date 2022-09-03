from flask_restful import Resource, reqparse
from app.models.user import UserModel
from flask import jsonify, request
from flask import Response, json
import jwt
import re
import datetime
from passlib.hash import sha256_crypt
from flask import current_app
from app.decorators import auth_required


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('access',
                        type=str
                        )

    @auth_required(1)
    def get(user, self, id):
        if user.access < 3 and int(user.id) != int(id):
            return {"message": 'Permission denied'}, 401
        else:
            return {'data': user.json()}


class AdminUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('access',
                        type=str
                        )

    @auth_required(3)
    def get(user, self, id):
        user = UserModel.find_by_id(id)
        if user:
            return user.json()
        else:
            return {"message": 'User not found'}, 201

    @auth_required(3)
    def patch(user, self, id):
        data = User.parser.parse_args()
        userX = UserModel.find_by_id(id)
        if userX:
            userX.access = int(data.access)
            userX.save_to_db()
        else:
            return {"message": 'User not found!'}, 201
        return {"message": 'user updated'}

    @auth_required(3)
    def delete(user, self, id):
        userX = UserModel.find_by_id(id)
        if userX:
            userX.delete_from_db()
            return {'message': 'user deleted.'}
        else:
            return {"message": 'User not found!'}, 201


# class controlling skills resource
class AdminUserList(Resource):
    @auth_required(3)
    def get(user, self):
        users = list(map(lambda x: x.json(), UserModel.query.all()))
        response = Response(json.dumps(users))
        response.headers['Content-Range'] = len(users)
        return response
