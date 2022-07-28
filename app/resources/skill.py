from flask_restful import Resource, reqparse
from app.models.skill import SkillModel
from app.decorators import auth_required

# class controlling skill resource
class Skill(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name')
    parser.add_argument('graph')
    parser.add_argument('equation')

    @auth_required(3)
    def post(user, self, id):
        data = Skill.parser.parse_args()
        skill = SkillModel(
            name = data['name'],
            graph = data['graph'],
            equation = data['equation']
        )
        try:
            skill.save_to_db()
        except:
            return {'message': 'Error with skill creation'}, 404
        return skill.json(), 201

    @auth_required(1)
    def get(user, self, id):
        skill = SkillModel.find_by_id(int(id))
        if skill:
            return skill.json()
        return {'message': 'Skill not found'}, 404

    @auth_required(3)
    def put(user, self, id):
        data = Skill.parser.parse_args()
        skill = SkillModel.find_by_id(int(id))
        if skill:
            skill.update(**data)
        else:
            {'message': 'Skill not found'}, 404
        skill.save_to_db()
        return skill.json()

    @auth_required(3)
    def delete(user, self, id):
        skill = SkillModel.find_by_id(int(id))
        if skill:
            skill.delete_from_db()
            return {'message': 'Skill deleted.'}
        return {'message': 'Skill not found.'}, 404

# class controlling skills resource
class SkillList(Resource):
    def get(self):
        skills = list(map(lambda x: x.summary(), SkillModel.query.all()))
        return {
            'skills': skills,
            'n_skills': len(skills)
        }
