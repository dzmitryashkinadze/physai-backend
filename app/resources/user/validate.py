from flask_restful import Resource
from app.models.user import UserModel
from flask import request
import jwt
from flask import current_app


class UserValidate(Resource):
    """
    This resource is used to validate users.
    Users must provide their JWT access token.
    It returns a message and a status code.
    """

    def get(self):
        """Validate a user and return a message and a status code"""

        auth_header = request.headers.get("Authorization")

        if auth_header:
            # Parses out the "Bearer" portion
            token = auth_header.split(" ")[1]
        else:
            token = ""
        if token:
            try:
                decoded = jwt.decode(
                    token, current_app.config["JWT_SECRET_KEY"], algorithms=["HS256"]
                )
            except jwt.ExpiredSignatureError:
                return {"message": "token expired", "auth": 0}, 401
            except jwt.InvalidTokenError:
                return {"message": "token invalid", "auth": 0}, 401
            if isinstance(decoded, dict):
                user = UserModel.find_by_email(decoded["email"])
                if not user:
                    return {"message": "token invalid", "auth": 0}, 401
                else:
                    return {
                        "message": "You are successfully logged in!",
                        "auth": user.role,
                        "user_id": user.id,
                    }
            else:
                return {"message": "token invalid", "auth": 0}, 401
        return {"message": "token missing", "auth": 0}, 401
