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
    """
    This resource is used to login users.
    Users must provide their email and password.
    It returns a JWT access token and a JWT refresh token.
    """

    # Create a parser for the incoming request
    parser = reqparse.RequestParser()
    parser.add_argument("access", type=str)

    @auth_required(1)
    def get(user, self, id):
        """Get a user"""

        if user.access < 3 and int(user.id) != int(id):
            return {"message": "Permission denied"}, 401
        else:
            return {"data": user.json()}
