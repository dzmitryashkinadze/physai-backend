from flask_restful import Resource
from app.models.user import UserModel
from flask import request
import jwt
from flask import current_app


class AdminValidate(Resource):
    """
    This resource is used to validate admins.
    """

    def get(self):
        """Validate an admin user"""

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
            if not isinstance(decoded, str):
                user = UserModel.find_by_email(decoded["email"])
                if not user:
                    return {"message": "token invalid", "auth": 0}, 401
                else:
                    if user.role != 3:
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
