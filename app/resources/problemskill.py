from flask_restful import Resource, reqparse
from app.models.problemskill import ProblemSkillModel
from app.models.skill import SkillModel
from app.decorators import auth_required


# class controlling skills resource
class ProblemSkillList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('skill_id')

    # get skills
    @auth_required(1)
    def get(user, self, problem_id):
        skill_list = list(map(lambda x: int(x.skill_id),
                              ProblemSkillModel.find_skills(problem_id)))
        skills = list(map(lambda x: SkillModel.find_by_id(x).summary(),
                          skill_list))
        return {
            'skills': skills,
            'n_skills': len(skills),
            'skill_array': skill_list
        }

    # add skills
    @auth_required(3)
    def post(user, self, problem_id):
        data = ProblemSkillList.parser.parse_args()
        skill_id = data['skill_id']
        skill = ProblemSkillModel(
            problem_id=problem_id,
            skill_id=skill_id
        )
        try:
            skill.save_to_db()
        except Exception:
            return {'message': 'Error with skill creation'}, 404
        return skill.json(), 201

    # delete skills
    @auth_required(3)
    def patch(user, self, problem_id):
        data = ProblemSkillList.parser.parse_args()
        skill_id = data['skill_id']
        skill = ProblemSkillModel.find_skill(problem_id, skill_id)
        if skill:
            skill.delete_from_db()
            return {'message': 'Skill deleted.'}
        return {'message': 'Skill not found.'}, 404
