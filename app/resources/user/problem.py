from flask_restful import Resource, reqparse
from app.models.problem import ProblemModel
from app.decorators import auth_required


# class controlling problem resource
class Problem(Resource):
    """
    This resource is used to get and solve a problem with details by id
    """

    # Create a parser for the incoming request
    parser = reqparse.RequestParser()
    parser.add_argument("bundle_id", type=int)
    parser.add_argument("text")
    parser.add_argument("graph")
    parser.add_argument("problem_number")
    parser.add_argument("access")
    parser.add_argument("difficulty")

    @auth_required(1)
    def get(user, self, id):
        """Get a problem by id"""

        # Find the problem by id
        problem = ProblemModel.find_by_id(int(id))
        if problem:
            if int(problem.access) > int(user.access):
                return {"message": "permission denied"}, 401
            else:
                return problem.json()
        return {"message": "Problem not found"}, 404

    @auth_required(1)
    def patch(user, self, id):
        """Solve a problem"""

        # Extract data
        data = Problem.parser.parse_args()
        problem = ProblemModel.find_by_id(int(id))

        # Check if graph exists and solve it
        if problem and "graph" in data and data["graph"]:
            result = problem.check_graph(data["graph"])
        else:
            {"message": "Something is wrong"}, 404
        return {"result": result}


class ProblemList(Resource):
    """
    This resource is used to get all problems
    """

    @auth_required(1)
    def get(user, self, bundle_id):
        """Get all problems in a bundle"""

        def takeProblemNumber(el):
            return el["problem_number"]

        # Request all problems
        problems = list(
            map(
                lambda x: x.summary(),
                ProblemModel.query.filter_by(bundle_id=bundle_id).all(),
            )
        )
        problems.sort(key=takeProblemNumber)
        return {"problems": problems, "n_problems": len(problems)}
