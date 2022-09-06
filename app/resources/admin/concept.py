from flask_restful import Resource, reqparse
from app.models.concept import ConceptModel
from app.models.updater import Updater
from flask import Response, json
from app.decorators import auth_required


class AdminConcept(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('frame_id', type=int)
    parser.add_argument('course_id', type=int)
    parser.add_argument('text', type=str)

    @auth_required(3)
    def get(user, self, id):
        raw = ConceptModel.find_by_id(int(id))
        if raw:
            return raw.json()
        return {'message': 'raw not found'}, 404

    @auth_required(3)
    def put(user, self, id):
        data = AdminConcept.parser.parse_args()
        raw = ConceptModel.find_by_id(int(id))
        if raw:
            raw.update(**data)
        else:
            {'message': 'raw not found'}, 404
        raw.save_to_db()
        return raw.json()

    @auth_required(3)
    def delete(user, self, id):
        raw = ConceptModel.find_by_id(int(id))
        if raw:
            raw.delete_from_db()
            return {'message': 'raw deleted.'}
        return {'message': 'raw not found.'}, 404


class AdminConceptList(Resource):
    @auth_required(3)
    def get(user, self):
        data = list(map(lambda x: x.json(), ConceptModel.query.all()))
        response = Response(json.dumps(data))
        response.headers['Content-Range'] = len(data)
        return response

    @auth_required(3)
    def post(user, self):
        data = AdminConcept.parser.parse_args()
        try:
            raw = ConceptModel(**data)
            raw.save_to_db()
        except Exception:
            return {'message': 'Error with raw creation'}, 404
        return raw.json(), 201
