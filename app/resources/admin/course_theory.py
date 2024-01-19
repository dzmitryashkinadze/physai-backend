from flask_restful import Resource, reqparse
from app.models.course_theory import CourseTheoryModel
from flask import Response, json
from app.decorators import auth_required


class AdminCourseTheory(Resource):
    """
    This resource is used to get, update and delete equations.
    """

    # Create a parser for the incoming request
    parser = reqparse.RequestParser()
    parser.add_argument("title", type=str)
    parser.add_argument("equation", type=str)
    parser.add_argument("description", type=str)
    parser.add_argument("visible", type=bool)

    @auth_required(3)
    def get(user, self, id):
        """Get a equation by id"""
        raw = CourseTheoryModel.find_by_id(int(id))
        if raw:
            return raw.json()
        return {"message": "raw not found"}, 404

    @auth_required(3)
    def put(user, self, id):
        """Update a equation by id"""
        data = AdminCourseTheory.parser.parse_args()
        raw = CourseTheoryModel.find_by_id(int(id))
        if raw:
            raw.update(**data)
        else:
            {"message": "raw not found"}, 404
        raw.save_to_db()
        return raw.json()

    @auth_required(3)
    def delete(user, self, id):
        """Delete a equation by id"""
        raw = CourseTheoryModel.find_by_id(int(id))
        if raw:
            raw.delete_from_db()
            return {"message": "raw deleted."}
        return {"message": "raw not found."}, 404


class AdminCourseTheoryList(Resource):
    """
    This resource is used to get, update and delete equations.
    """

    @auth_required(3)
    def get(user, self):
        """Get all equations"""

        data = list(map(lambda x: x.json(), CourseTheoryModel.query.all()))
        response = Response(json.dumps(data))
        response.headers["Content-Range"] = len(data)
        return response

    @auth_required(3)
    def post(user, self):
        """Create a equation"""

        data = AdminCourseTheory.parser.parse_args()
        try:
            raw = CourseTheoryModel(**data)
            raw.save_to_db()
        except Exception:
            return {"message": "Error with raw creation"}, 404
        return raw.json(), 201
