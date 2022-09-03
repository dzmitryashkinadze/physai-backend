from flask_restful import Resource, reqparse
from app.models.problem_equation import ProblemEquationModel
from flask import Response, json
from app.decorators import auth_required


class AdminProblemEquation(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('problem_id', type=int)
    parser.add_argument('equation_id', type=int)

    @auth_required(3)
    def get(user, self, id):
        raw = ProblemEquationModel.find_by_id(int(id))
        if raw:
            return raw.json()
        return {'message': 'Problem not found'}, 404

    @auth_required(3)
    def put(user, self, id):
        data = AdminProblemEquation.parser.parse_args()
        problem = ProblemEquationModel.find_by_id(int(id))
        if problem:
            problem.update(**data)
        else:
            {'message': 'Problem not found'}, 404
        problem.save_to_db()
        return problem.json()

    @auth_required(3)
    def delete(user, self, id):
        raw = ProblemEquationModel.find_by_id(int(id))
        if raw:
            raw.delete_from_db()
            return {'message': 'Problem deleted.'}
        return {'message': 'Problem not found.'}, 404


class AdminProblemEquationList(Resource):
    @auth_required(3)
    def get(user, self):
        data = list(
            map(lambda x: x.json(), ProblemEquationModel.query.all()))
        response = Response(json.dumps(data))
        response.headers['Content-Range'] = len(data)
        return response

    @auth_required(3)
    def post(user, self):
        data = AdminProblemEquation.parser.parse_args()
        try:
            raw = ProblemEquationModel(
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
