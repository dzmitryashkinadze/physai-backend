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


class UserAdmin(Resource):
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


class UserValidate(Resource):
    def get(self):

        auth_header = request.headers.get('Authorization')
        if auth_header:
            token = auth_header.split(" ")[1] # Parses out the "Bearer" portion
        else:
            token = ''
        if token:
            try:
                decoded = jwt.decode(token, current_app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
            except jwt.ExpiredSignatureError:
                return {'message': 'token expired',
                        'auth': 0}
            except jwt.InvalidTokenError:
                return {'message': 'token invalid',
                        'auth': 0}
            if not isinstance(decoded, str):
                user = UserModel.find_by_email(decoded['email'])
                if not user:
                    return {'message': 'token invalid',
                            'auth': 0}
                else:
                    return {'message': 'You are successfully logged in!',
                            'auth': user.access,
                            'user_id': user.id}
            else:
                return {'message': 'token invalid',
                        'auth': 0}
        return {'message': 'token missing',
                'auth': 0}


class UserRegister(Resource):
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
        data = UserRegister.parser.parse_args()
        validity = True
        status = 0
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(regex, data['email']):
            validity = False
            message = "Неверный формат электронной почты"
            status = 1
        if UserModel.find_by_email(data['email']):
            validity = False
            message = "Учетная запись с этой электронной почтой уже существуют"
            status = 2
        if len(data['password']) < 6:
            validity = False
            message = "Пароль должен быть не короче 6 знаков"
            status = 3
        if validity:
            user = UserModel(
                email=data['email'],
                password=sha256_crypt.hash(data['password']),
                access=1
            )
            user.save_to_db()
            message = "Учетная запись успешна зарегистрирована"
        return {"message": message,
                "status": status}


class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="This field cannot be blank.")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank.")
    parser.add_argument('keep_in_system',
                        type=bool,
                        required=True,
                        help="This field cannot be blank.")

    def post(self):
        data = UserLogin.parser.parse_args()
        user = UserModel.find_by_email(data['email'])
        if not (user and sha256_crypt.verify(data['password'], user.password)):
            return {"message": "Bad email or password",
                    "status": 1}
        access_payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0,
                                                                   minutes=30),
            'iat': datetime.datetime.utcnow(),
            'access': user.access,
            'email': data['email']
        }
        if data['keep_in_system']:
            refresh_validity_days = 7
        else:
            refresh_validity_days = 1
        refresh_payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=refresh_validity_days,
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
                "refresh_token": refresh_token,
                "user_id": user.id,
                "access": user.access}


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
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0,
                                                                   minutes=60),
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


class UserRefresh(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('refreshToken',
                        type=str,
                        required=True,
                        help="This field cannot be blank.")

    def post(self):
        data = UserRefresh.parser.parse_args()
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
                        datetime.timedelta(days=0, minutes=30),
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
class UserListAdmin(Resource):
    @auth_required(3)
    def get(user, self):
        users = list(map(lambda x: x.json(), UserModel.query.all()))
        response = Response(json.dumps(users))
        response.headers['Content-Range'] = len(users)
        return response
