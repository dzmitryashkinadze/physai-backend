from flask_restful import Resource, reqparse
from app.models.group import GroupModel
from flask import Response, json
from app.decorators import auth_required


class AdminGroup(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str)
    parser.add_argument('visible', type=bool)
    parser.add_argument('description', type=str)
    parser.add_argument('sequence_id', type=int)

    @auth_required(3)
    def get(user, self, id):
        raw = GroupModel.find_by_id(int(id))
        if raw:
            return raw.json()
        return {'message': 'raw not found'}, 404

    @auth_required(3)
    def put(user, self, id):
        data = AdminGroup.parser.parse_args()
        raw = GroupModel.find_by_id(int(id))
        if raw:
            if data["sequence_id"] is None:
                data["sequence_id"] = raw.sequence_id
            print(data)
            raw.update(**data)
        else:
            {'message': 'raw not found'}, 404
        raw.save_to_db()
        return raw.json()

    @auth_required(3)
    def delete(user, self, id):
        raw = GroupModel.find_by_id(int(id))
        if raw:
            raw.delete_from_db()
            return {'message': 'raw deleted.'}
        return {'message': 'raw not found.'}, 404


class AdminGroupList(Resource):
    @auth_required(3)
    def get(user, self):
        data = list(map(lambda x: x.json(), GroupModel.query.order_by(
            GroupModel.sequence_id).all()))
        response = Response(json.dumps(data))
        response.headers['Content-Range'] = len(data)
        return response

    @auth_required(3)
    def post(user, self):
        data = AdminGroup.parser.parse_args()
        try:
            if data["sequence_id"] is None:
                # check highest sequence_id and set this one highest + 1
                test = list(map(lambda x: x.json(), GroupModel.query.order_by(
                    GroupModel.sequence_id).all()))
                data["sequence_id"] = test[-1]["sequence_id"] + 1
            raw = GroupModel(**data)
            raw.save_to_db()
        except Exception:
            return {'message': 'Error with raw creation'}, 404
        return raw.json(), 201
