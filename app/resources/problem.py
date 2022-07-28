from flask_restful import Resource, reqparse
from app.models.problem import ProblemModel
from app.decorators import auth_required


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# class controlling problem resource
class Problem(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('bundle_id', type=int)
    parser.add_argument('text')
    parser.add_argument('graph')
    parser.add_argument('problem_number')
    parser.add_argument('access')
    parser.add_argument('difficulty')

    @auth_required(3)
    def post(user, self, id):
        data = Problem.parser.parse_args()
        try:
            problem = ProblemModel(
                bundle_id=data['bundle_id'],
                text=data['text'],
                graph=data['graph'],
                problem_number=data['problem_number'],
                access=data['access'],
                difficulty=data['difficulty']
            )
            problem.save_to_db()
        except Exception:
            return {'message': 'Error with problem creation'}, 404
        return problem.json(), 201

    @auth_required(1)
    def get(user, self, id):
        problem = ProblemModel.find_by_id(int(id))
        if problem:
            if int(problem.access) > int(user.access):
                return {'message': 'permission denied'}, 401
            else:
                return problem.json()
        return {'message': 'Problem not found'}, 404

    @auth_required(1)
    def patch(user, self, id):
        data = Problem.parser.parse_args()
        problem = ProblemModel.find_by_id(int(id))
        if problem and 'graph' in data and data['graph']:
            result = problem.check_graph(data['graph'])
        else:
            {'message': 'Something is wrong'}, 404
        return {'result': result}

    @auth_required(3)
    def put(user, self, id):
        data = Problem.parser.parse_args()
        problem = ProblemModel.find_by_id(int(id))
        if problem:
            problem.update(**data)
        else:
            {'message': 'Problem not found'}, 404
        problem.save_to_db()
        return problem.json()

    @auth_required(3)
    def delete(user, self, id):
        problem = ProblemModel.find_by_id(int(id))
        if problem:
            problem.delete_from_db()
            return {'message': 'Problem deleted.'}
        return {'message': 'Problem not found.'}, 404


# class controlling problems resource
class ProblemList(Resource):
    @auth_required(1)
    def get(user, self, bundle_id):
        def takeProblemNumber(el):
            return el['problem_number']
        problems = list(map(lambda x: x.summary(),
                            ProblemModel.query.
                            filter_by(bundle_id=bundle_id).all()))
        problems.sort(key=takeProblemNumber)
        return {
            'problems': problems,
            'n_problems': len(problems)
        }


# class controlling problems resource
class ProblemListAdmin(Resource):
    @auth_required(3)
    def get(user, self, bundle_id):
        def takeProblemNumber(el):
            return el['problem_number']
        problems = list(map(lambda x: x.summary(),
                            ProblemModel.query.
                            filter_by(bundle_id=bundle_id).all()))
        problems.sort(key=takeProblemNumber)
        return {
            'problems': problems,
            'n_problems': len(problems)
        }
