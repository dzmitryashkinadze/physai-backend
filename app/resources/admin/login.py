from flask_restful import Resource, reqparse
from app.models.user import UserModel
import jwt
import datetime
from passlib.hash import sha256_crypt
from flask import current_app


class AdminLogin(Resource):
    """
    This resource is used to login users.
    Users must provide their email and password.
    It returns a JWT access token and a JWT refresh token.
    """

    # Create a parser for the incoming request
    parser = reqparse.RequestParser()

    # Add 'email' argument to the parser
    parser.add_argument(
        "email", type=str, required=True, help="This field cannot be blank."
    )

    # Add 'password' argument to the parser
    parser.add_argument(
        "password", type=str, required=True, help="This field cannot be blank."
    )

    def post(self):
        """Login a user and return a JWT access token and a JWT refresh token"""

        # Parse the incoming request and get user
        data = AdminLogin.parser.parse_args()

        user = UserModel.find_by_email(data["email"])

        # Verify that the user is admin
        if user.role != 3:
            return {"message": "Bad email or password", "status": 1}

        # Verify the password
        if not (user and sha256_crypt.verify(data["password"], user.password_hash)):
            return {"message": "Bad email or password", "status": 1}

        # Create the payload for the access token
        access_payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=30),
            "iat": datetime.datetime.utcnow(),
            "role": user.role,
            "email": data["email"],
        }

        # Create the payload for the refresh token
        refresh_validity_days = 7
        refresh_payload = {
            "exp": datetime.datetime.utcnow()
            + datetime.timedelta(days=refresh_validity_days, minutes=0),
            "iat": datetime.datetime.utcnow(),
            "role": user.role,
            "email": data["email"],
        }

        # Encode the access token
        access_token = jwt.encode(
            access_payload, current_app.config["JWT_SECRET_KEY"], algorithm="HS256"
        )

        # Encode the refresh token
        refresh_token = jwt.encode(
            refresh_payload, current_app.config["JWT_SECRET_KEY"], algorithm="HS256"
        )

        # Return the response
        return {
            "message": "Login granted",
            "status": 0,
            "access_token": access_token,
            "refresh_token": refresh_token,
            "user_id": user.id,
            "role": user.role,
        }
