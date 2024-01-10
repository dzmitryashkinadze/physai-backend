from flask_restful import Resource, reqparse
from flask import jsonify, request
from flask import Response, json
import jwt
import re
import datetime
from passlib.hash import sha256_crypt
from flask import current_app
from app.decorators import auth_required
from app.models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "email", type=str, required=True, help="This field cannot be blank."
    )
    parser.add_argument(
        "password", type=str, required=True, help="This field cannot be blank."
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        validity = True
        status = 0
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        if not re.fullmatch(regex, data["email"]):
            validity = False
            message = "Wrong email format"
            status = 1
        if UserModel.find_by_email(data["email"]):
            validity = False
            message = "Account with this email already exists"
            status = 2
        if len(data["password"]) < 6:
            validity = False
            message = "Password must be at least 6 characters long"
            status = 3
        if validity:
            user = UserModel(
                email=data["email"], password_hash=sha256_crypt.hash(data["password"])
            )
            user.save_to_db()
            message = "Account created successfully"
        return {"message": message, "status": status}
