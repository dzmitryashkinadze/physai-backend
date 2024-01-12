from flask_restful import Resource, reqparse
from app.decorators import auth_required
from app.models.user_progress_course import UserProgressCourseModel
from app.models.user_progress_problem import UserProgressProblemModel


class UserProgress(Resource):
    """
    This resource is used to get and update user progress
    """

    # Create a parser for the incoming request
    parser = reqparse.RequestParser()
    parser.add_argument("progress")

    # get user progress
    @auth_required(1)
    def get(user, self, id):
        """Get user progress"""

        try:
            progress_model = UserProgressCourseModel.find_progress(user.id, id)
            progress = progress_model.progress
        except:
            progress_model = UserProgressCourseModel(
                user_id=user.id, bundle_id=int(id), progress=0
            )
            progress_model.save_to_db()
            progress = 0
        return {"progress": progress}

    # update user progress
    @auth_required(1)
    def put(user, self, id):
        """Update user progress"""

        data = UserProgress.parser.parse_args()
        progress_model = UserProgressCourseModel.find_progress(user.id, id)
        if progress_model:
            # update model
            progress_model.progress = data["progress"]
        elif data["progress"]:
            # user_id, bundle_id, progress
            progress_model = UserProgressCourseModel(
                user_id=user.id, bundle_id=id, progress=data["progress"]
            )
        else:
            return {"message": "no progress found"}, 201
        # save the instance
        progress_model.save_to_db()
        return progress_model.json()


class UserProgressList(Resource):
    """
    This resource is used to get all user progress
    """

    @auth_required(1)
    def get(user, self):
        """Get all user progress"""

        progress_list = list(
            map(
                lambda x: x.json(),
                UserProgressCourseModel.query.filter_by(user_id=user.id).all(),
            )
        )
        return progress_list
