from flask_restful import Resource, reqparse
from app.models.course import CourseModel
from flask import Response, json
from app.decorators import auth_required


class AdminCourse(Resource):
    """
    This resource is used to get, update and delete courses.
    """

    # Create a parser for the incoming request
    parser = reqparse.RequestParser()
    parser.add_argument("title", type=str)
    parser.add_argument("summary", type=str)
    parser.add_argument("description", type=str)
    parser.add_argument("visible", type=bool)

    # native features
    native_features = [
        "title",
        "summary",
        "description",
        "visible",
        "logo_path",
        "group_id",
        "sequence",
    ]

    @auth_required(3)
    def get(user, self, id):
        """Get a course by id"""

        raw = CourseModel.find_by_id(int(id))
        if raw:
            return raw.json()
        return {"message": "raw not found"}, 404

    @auth_required(3)
    def put(user, self, id):
        """Update a course by id"""

        data = AdminCourse.parser.parse_args()
        print(data)
        data_native = {
            k: v for k, v in data.items() if k in AdminCourse.native_features
        }
        print(data_native)
        raw = CourseModel.find_by_id(int(id))
        if raw:
            raw.update(**data_native)
        else:
            {"message": "raw not found"}, 404
        raw.save_to_db()
        return raw.json()

    @auth_required(3)
    def delete(user, self, id):
        """Delete a course by id"""

        raw = CourseModel.find_by_id(int(id))
        if raw:
            raw.delete_from_db()
            return {"message": "raw deleted."}
        return {"message": "raw not found."}, 404


class AdminCourseList(Resource):
    """
    This resource is used to get, update and delete courses.
    """

    @auth_required(3)
    def get(user, self):
        """Get all courses"""

        data = list(map(lambda x: x.json(), CourseModel.query.all()))
        response = Response(json.dumps(data))
        response.headers["Content-Range"] = len(data)
        return response

    @auth_required(3)
    def post(user, self):
        """Create a course"""

        data = AdminCourse.parser.parse_args()
        try:
            raw = CourseModel(**data)
            raw.save_to_db()
        except Exception:
            return {"message": "Error with raw creation"}, 404
        return raw.json(), 201
