from flask_restful import Resource, reqparse
from app.models.problem import ProblemModel
from flask import Response, json
from app.decorators import auth_required


class AdminProblem(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('description', type=str)
    parser.add_argument('explanation', type=str)
    parser.add_argument('solution', type=str)
    parser.add_argument('frame_id', type=int)
    parser.add_argument('visible', type=bool)

    @auth_required(3)
    def get(user, self, id):
        raw = ProblemModel.find_by_id(int(id))
        if raw:
            return raw.json()
        return {'message': 'Problem not found'}, 404

    @auth_required(3)
    def put(user, self, id):
        data = AdminProblem.parser.parse_args()
        problem = ProblemModel.find_by_id(int(id))
        if problem:
            problem.update(**data)
        else:
            {'message': 'Problem not found'}, 404
        problem.save_to_db()
        return problem.json()

    @auth_required(3)
    def delete(user, self, id):
        raw = ProblemModel.find_by_id(int(id))
        if raw:
            raw.delete_from_db()
            return {'message': 'Problem deleted.'}
        return {'message': 'Problem not found.'}, 404


class AdminProblemList(Resource):
    @auth_required(3)
    def get(user, self):
        data = list(map(lambda x: x.json(), ProblemModel.query.all()))
        response = Response(json.dumps(data))
        response.headers['Content-Range'] = len(data)
        return response

    @auth_required(3)
    def post(user, self):
        data = AdminProblem.parser.parse_args()
        try:
            raw = ProblemModel(
                bundle_id=data['bundle_id'],
                text=data['text'],
                graph=data['graph'],
                problem_number=data['problem_number'],
                access=data['access'],
                difficulty=data['difficulty']
            )
            raw.save_to_db()
        except Exception:
            return {'message': 'Error with problem creation'}, 404
        return raw.json(), 201
