from flask_restful import Resource, reqparse
import re
from passlib.hash import sha256_crypt
from app.models.user import UserModel


class UserRegister(Resource):
    """
    This resource is used to register a user
    """

    # Create a parser for the incoming request
    parser = reqparse.RequestParser()
    parser.add_argument(
        "email", type=str, required=True, help="This field cannot be blank."
    )
    parser.add_argument(
        "password", type=str, required=True, help="This field cannot be blank."
    )

    def post(self):
        """Register a user"""

        # Get the data from the parser
        data = UserRegister.parser.parse_args()

        # validate the email
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

        # validate the password
        if len(data["password"]) < 6:
            validity = False
            message = "Password must be at least 6 characters long"
            status = 3

        # save the user to the database
        if validity:
            user = UserModel(
                email=data["email"], password_hash=sha256_crypt.hash(data["password"])
            )
            user.save_to_db()
            message = "Account created successfully"
        return {"message": message, "status": status}
