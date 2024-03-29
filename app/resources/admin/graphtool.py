from flask_restful import Resource, reqparse
from app.models.graphtool import GraphtoolModel
from flask import Response, json
from app.decorators import auth_required


class AdminGraphtool(Resource):
    """
    This resource is used to get, update and delete admin problem.
    """

    # Create a parser for the incoming request
    parser = reqparse.RequestParser()
    parser.add_argument("graphtool", type=str)

    @auth_required(3)
    def get(user, self, id):
        """Get a problem by id"""

        raw = GraphtoolModel.find_by_id(int(id))
        if raw:
            return raw.json()
        return {"message": "raw not found"}, 404

    @auth_required(3)
    def put(user, self, id):
        """Update a problem by id"""

        data = AdminGraphtool.parser.parse_args()
        raw = GraphtoolModel.find_by_id(int(id))
        if raw:
            raw.update(**data)
        else:
            {"message": "raw not found"}, 404
        raw.save_to_db()
        return raw.json()

    @auth_required(3)
    def delete(user, self, id):
        """Delete a problem by id"""

        raw = GraphtoolModel.find_by_id(int(id))
        if raw:
            raw.delete_from_db()
            return {"message": "raw deleted."}
        return {"message": "raw not found."}, 404


class AdminGraphtoolList(Resource):
    @auth_required(3)
    def get(user, self):
        """Get all problems"""

        data = list(map(lambda x: x.json(), GraphtoolModel.query.all()))
        response = Response(json.dumps(data))
        response.headers["Content-Range"] = len(data)
        return response

    @auth_required(3)
    def post(user, self):
        """Create a problem"""

        data = AdminGraphtool.parser.parse_args()
        try:
            raw = GraphtoolModel(**data)
            raw.save_to_db()
        except Exception:
            return {"message": "Error with raw creation"}, 404
        return raw.json(), 201
