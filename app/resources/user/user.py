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
    parser.add_argument("access", type=str)

    @auth_required(1)
    def get(user, self, id):
        if user.access < 3 and int(user.id) != int(id):
            return {"message": "Permission denied"}, 401
        else:
            return {"data": user.json()}
