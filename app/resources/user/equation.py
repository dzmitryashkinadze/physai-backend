from flask_restful import Resource
from app.models.equation import EquationModel
from app.decorators import auth_required


class Equation(Resource):
    """
    This resource is used to get an equation
    """

    @auth_required(1)
    def get(user, self, id):
        """Get an equation by id"""
        skill = EquationModel.find_by_id(int(id))
        if skill:
            return skill.json()
        return {"message": "Skill not found"}, 404


class EquationList(Resource):
    """
    This resource is get a list of equaitons
    """

    def get(self):
        """Get all equations"""
        skills = list(map(lambda x: x.summary(), EquationModel.query.all()))
        return {"skills": skills, "n_skills": len(skills)}
