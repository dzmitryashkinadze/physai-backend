from app.database import db
from sqlalchemy.sql import func


class ProblemEquationModel(db.Model):
    __tablename__ = "problem_equation"

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    problem_id = db.Column(db.Integer, db.ForeignKey('problem.id'))
    equation_id = db.Column(db.Integer, db.ForeignKey('equation.id'))
    time_created = db.Column(db.DateTime(timezone=False),
                             server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=False),
                             onupdate=func.now())

    def __init__(self, **kwargs):
        super(ProblemEquationModel, self).__init__(**kwargs)

    def json(self):
        return {
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
