from flask_restful import Resource, reqparse
from app.models.graph_equation import ProblemEquationModel
from app.models.equation import EquationModel
from app.decorators import auth_required


# class controlling skills resource
class ProblemEquationList(Resource):
    """
    This resource is used to get a list of equations for a problem.
    """

    # Create a parser for the incoming request
    parser = reqparse.RequestParser()
    parser.add_argument("skill_id")

    # get skills
    @auth_required(1)
    def get(user, self, problem_id):
        """Get all equaitons for a problem"""

        skill_list = list(
            map(lambda x: int(x.skill_id), ProblemEquationModel.find_skills(problem_id))
        )
        skills = list(map(lambda x: EquationModel.find_by_id(x).summary(), skill_list))
        return {"skills": skills, "n_skills": len(skills), "skill_array": skill_list}
