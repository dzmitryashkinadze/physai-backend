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
        if not (user and sha256_crypt.verify(data['password'], user.password_hash)):
            return {"message": "Bad email or password",
                    "status": 1}
        access_payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0,
                                                                   minutes=30),
            'iat': datetime.datetime.utcnow(),
            'role': user.role,
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
            'role': user.role,
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
                "role": user.role}
