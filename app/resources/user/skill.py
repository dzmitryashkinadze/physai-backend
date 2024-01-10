from flask_restful import Resource, reqparse
from flask import Response, json
from app.models.skill import SkillModel
from app.decorators import auth_required


# class controlling skill resource
class Skill(Resource):
    @auth_required(1)
    def get(user, self, id):
        skill = SkillModel.find_by_id(int(id))
        if skill:
            return skill.json()
        return {"message": "Skill not found"}, 404


# class controlling skills resource
class SkillList(Resource):
    def get(self):
        skills = list(map(lambda x: x.summary(), SkillModel.query.all()))
        return {"skills": skills, "n_skills": len(skills)}
