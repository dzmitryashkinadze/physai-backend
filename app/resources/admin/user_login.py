from flask_restful import Resource, reqparse
from app.models.user_login import UserLoginModel
from app.decorators import auth_required


# class controlling skills resource
class AdminUserLoginList(Resource):
    """
    This resource is used to get a list of equations for a problem.
    """

    # get skills
    @auth_required(3)
    def get(user, self):
        """Get all relations between problems and equations"""

        data = list(map(lambda x: x.json(), UserLoginModel.query.all()))
        return data
