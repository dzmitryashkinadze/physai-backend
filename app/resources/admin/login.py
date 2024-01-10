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


class AdminLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "email", type=str, required=True, help="This field cannot be blank."
    )
    parser.add_argument(
        "password", type=str, required=True, help="This field cannot be blank."
    )

    def post(self):
        data = AdminLogin.parser.parse_args()
        user = UserModel.find_by_email(data["email"])
        if not (user and sha256_crypt.verify(data["password"], user.password_hash)):
            return {"message": "Bad email or password", "status": 1}
        if not (int(user.role) == 3):
            return {"message": "Bad email or password", "status": 1}
        access_payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1, minutes=0),
            "iat": datetime.datetime.utcnow(),
            "access": user.role,
            "email": data["email"],
        }
        refresh_payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=30, minutes=0),
            "iat": datetime.datetime.utcnow(),
            "access": user.role,
            "email": data["email"],
        }
        access_token = jwt.encode(
            access_payload, current_app.config["JWT_SECRET_KEY"], algorithm="HS256"
        )
        refresh_token = jwt.encode(
            refresh_payload, current_app.config["JWT_SECRET_KEY"], algorithm="HS256"
        )
        return {
            "message": "Login granted",
            "status": 0,
            "access_token": access_token,
            "refresh_token": refresh_token,
        }
