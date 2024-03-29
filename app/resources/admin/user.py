from flask_restful import Resource, reqparse
from app.models.user import UserModel
from flask import Response, json
from app.decorators import auth_required


class AdminUser(Resource):
    """
    This resource is used to get, update and delete admins.
    """

    # Create a parser for the incoming request
    parser = reqparse.RequestParser()
    parser.add_argument("role", type=int)

    @auth_required(3)
    def get(user, self, id):
        """Get an admin user by id"""

        raw = UserModel.find_by_id(int(id))
        if raw:
            return raw.json()
        return {"message": "raw not found"}, 404

    @auth_required(3)
    def put(user, self, id):
        """Update an admin user by id"""

        data = AdminUser.parser.parse_args()
        raw = UserModel.find_by_id(int(id))
        if raw:
            raw.update(**data)
        else:
            {"message": "raw not found"}, 404
        raw.save_to_db()
        return raw.json()

    @auth_required(3)
    def delete(user, self, id):
        """Delete an admin user by id"""

        raw = UserModel.find_by_id(int(id))
        if raw:
            raw.delete_from_db()
            return {"message": "raw deleted."}
        return {"message": "raw not found."}, 404


class AdminUserList(Resource):
    @auth_required(3)
    def get(user, self):
        data = list(map(lambda x: x.json(), UserModel.query.all()))
        response = Response(json.dumps(data))
        response.headers["Content-Range"] = len(data)
        return response
