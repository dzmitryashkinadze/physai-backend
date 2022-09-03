from flask_restful import Resource
from app.models.group import GroupModel
from flask import Response, json


class GroupList(Resource):
    def get(self):
        groups = list(map(lambda x: x.json(), GroupModel.query.all()))
        response = Response(json.dumps(groups))
        response.headers['Content-Range'] = len(groups)
        return response
