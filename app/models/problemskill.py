from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from app import db
import json

class ProblemSkillModel(db.Model):
    __tablename__ = 'problem_skills'

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    problem_id = db.Column(db.Integer)
    skill_id = db.Column(db.Integer)

    def __init__(self, problem_id, skill_id):
        self.problem_id = problem_id
        self.skill_id = skill_id

    # output
    def json(self):
        return {
            'problem_id': self.problem_id,
            'skill_id': self.skill_id
        }

    # finder
    @classmethod
    def find_skills(cls, problem_id):
        return cls.query.filter_by(problem_id=problem_id).all()

    # finder
    @classmethod
    def find_skill(cls, problem_id, skill_id):
        return cls.query.\
            filter_by(problem_id=problem_id).\
            filter_by(skill_id=skill_id).\
            first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
