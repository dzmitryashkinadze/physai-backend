from flask_restful import Resource, reqparse
from flask import Response, json
from app.models.user_progress import UserProgressModel
from app.decorators import auth_required
from flask import request


# class controlling skills resource
class UserProgress(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("progress")

    # get user progress
    @auth_required(1)
    def get(user, self, id):
        try:
            progress_model = UserProgressModel.find_progress(user.id, id)
            progress = progress_model.progress
        except:
            progress_model = UserProgressModel(
                user_id=user.id, bundle_id=int(id), progress=0
            )
            progress_model.save_to_db()
            progress = 0
        return {"progress": progress}

    # update user progress
    @auth_required(1)
    def put(user, self, id):
        data = UserProgress.parser.parse_args()
        progress_model = UserProgressModel.find_progress(user.id, id)
        if progress_model:
            # update model
            progress_model.progress = data["progress"]
        elif data["progress"]:
            # user_id, bundle_id, progress
            progress_model = UserProgressModel(
                user_id=user.id, bundle_id=id, progress=data["progress"]
            )
        else:
            return {"message": "no progress found"}, 201
        # save the instance
        progress_model.save_to_db()
        return progress_model.json()


class UserProgressList(Resource):
    @auth_required(1)
    def get(user, self):
        progress_list = list(
            map(
                lambda x: x.json(),
                UserProgressModel.query.filter_by(user_id=user.id).all(),
            )
        )
        return progress_list
