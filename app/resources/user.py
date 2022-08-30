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


class AdminValidate(Resource):
    def get(self):

        auth_header = request.headers.get('Authorization')
        if auth_header:
            # Parses out the "Bearer" portion
            token = auth_header.split(" ")[1]
        else:
            token = ''
        if token:
            try:
                decoded = jwt.decode(
                    token, current_app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
            except jwt.ExpiredSignatureError:
                return {'message': 'token expired',
                        'auth': 0}, 401
            except jwt.InvalidTokenError:
                return {'message': 'token invalid',
                        'auth': 0}, 401
            if not isinstance(decoded, str):
                user = UserModel.find_by_email(decoded['email'])
                if not user:
                    return {'message': 'token invalid',
                            'auth': 0}, 401
                else:
                    if user.access != 3:
                        return {'message': 'token invalid',
                                'auth': 0}, 401
                    else:
                        return {'message': 'You are successfully logged in!',
                                'auth': user.access,
                                'user_id': user.id}
            else:
                return {'message': 'token invalid',
                        'auth': 0}, 401
        return {'message': 'token missing',
                'auth': 0}, 401


class AdminLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = AdminLogin.parser.parse_args()
        user = UserModel.find_by_email(data['email'])
        if not (user and sha256_crypt.verify(data['password'], user.password)):
            return {"message": "Bad email or password",
                    "status": 1}
        if not (int(user.access) == 3):
            return {"message": "Bad email or password",
                    "status": 1}
        access_payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1,
                                                                   minutes=0),
            'iat': datetime.datetime.utcnow(),
            'access': user.access,
            'email': data['email']
        }
        refresh_payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30,
                                                                   minutes=0),
            'iat': datetime.datetime.utcnow(),
            'access': user.access,
            'email': data['email']
        }
        access_token = jwt.encode(access_payload,
                                  current_app.config['JWT_SECRET_KEY'],
                                  algorithm='HS256')
        refresh_token = jwt.encode(refresh_payload,
                                   current_app.config['JWT_SECRET_KEY'],
                                   algorithm='HS256')
        return {"message": "Login granted",
                "status": 0,
                "access_token": access_token,
                "refresh_token": refresh_token}


class AdminRefreshToken(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('refreshToken',
                        type=str,
                        required=True,
                        help="This field cannot be blank.")

    def post(self):
        data = AdminRefreshToken.parser.parse_args()
        if data['refreshToken']:
            token = data['refreshToken']
        else:
            token = ''
        if token:
            try:
                decoded = jwt.decode(token,
                                     current_app.config['JWT_SECRET_KEY'],
                                     algorithms=['HS256'])
            except jwt.ExpiredSignatureError:
                return jsonify({'message': 'Signature expired. Login please',
                                'auth': 0})
            except jwt.InvalidTokenError:
                return jsonify({'message': 'Nice try, invalid token. Login please',
                                'auth': 0})
            if not isinstance(decoded, str):
                user = UserModel.find_by_email(decoded['email'])
                if not user:
                    return jsonify({'message': 'Invalid token',
                                    'auth': 0})
                else:
                    access_payload = {
                        'exp': datetime.datetime.utcnow() +
                        datetime.timedelta(days=1, minutes=0),
                        'iat': datetime.datetime.utcnow(),
                        'access': user.access,
                        'email': user.email
                    }
                    access_token = jwt.encode(
                        access_payload,
                        current_app.config['JWT_SECRET_KEY'],
                        algorithm='HS256')
                    return jsonify({'message': 'Token refreshed',
                                    'accessToken': access_token})
            else:
                return jsonify({'message': 'Ooops, validation messed up: ' +
                                           decoded,
                                'auth': 0})
        return jsonify({
            'message': 'You do not have a token, but we are happy to have you here!',
            'auth': 0})


# class controlling skills resource
class AdminUserList(Resource):
    @auth_required(3)
    def get(user, self):
        users = list(map(lambda x: x.json(), UserModel.query.all()))
        response = Response(json.dumps(users))
        response.headers['Content-Range'] = len(users)
        return response
