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


class UserRefreshToken(Resource):
    """
    This resource is used to refresh a token
    """

    # Create a parser for the incoming request
    parser = reqparse.RequestParser()
    parser.add_argument(
        "refreshToken", type=str, required=True, help="This field cannot be blank."
    )

    def post(self):
        """Refresh a token"""

        data = UserRefreshToken.parser.parse_args()
        if data["refreshToken"]:
            token = data["refreshToken"]
        else:
            token = ""
        if token:
            try:
                decoded = jwt.decode(
                    token, current_app.config["JWT_SECRET_KEY"], algorithms=["HS256"]
                )
            except jwt.ExpiredSignatureError:
                return jsonify(
                    {"message": "Signature expired. Login please", "auth": 0}
                )
            except jwt.InvalidTokenError:
                return jsonify(
                    {"message": "Nice try, invalid token. Login please", "auth": 0}
                )
            if not isinstance(decoded, str):
                user = UserModel.find_by_email(decoded["email"])
                if not user:
                    return jsonify({"message": "Invalid token", "auth": 0})
                else:
                    access_payload = {
                        "exp": datetime.datetime.utcnow()
                        + datetime.timedelta(days=0, minutes=30),
                        "iat": datetime.datetime.utcnow(),
                        "role": user.role,
                        "email": user.email,
                    }
                    access_token = jwt.encode(
                        access_payload,
                        current_app.config["JWT_SECRET_KEY"],
                        algorithm="HS256",
                    )
                    return jsonify(
                        {"message": "Token refreshed", "accessToken": access_token}
                    )
            else:
                return jsonify(
                    {"message": "Ooops, validation messed up: " + decoded, "auth": 0}
                )
        return jsonify(
            {
                "message": "You do not have a token, but we are happy to have you here!",
                "auth": 0,
            }
        )
