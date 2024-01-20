from flask_restful import Resource, reqparse
from app.models.user_progress_theory import UserProgressTheoryModel
from app.decorators import auth_required


# class controlling skills resource
class AdminUserProgressTheoryList(Resource):
    """
    This resource is used to get a list of equations for a problem.
    """

    # get skills
    @auth_required(3)
    def get(user, self):
        """Get all relations between problems and equations"""

        data = list(map(lambda x: x.json(), UserProgressTheoryModel.query.all()))
        return data
