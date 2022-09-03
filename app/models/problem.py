from app.database import db
from sqlalchemy.sql import func


class ProblemModel(db.Model):
    __tablename__ = "problem"

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    frame_id = db.Column(db.Integer, db.ForeignKey('frame.id'))
    description = db.Column(db.String(255))
    explanation = db.Column(db.String(255))
    solution = db.Column(db.String(255))
    visible = db.Column(db.Boolean, default=False)
    time_created = db.Column(db.DateTime(timezone=False),
                             server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=False),
                             onupdate=func.now())

    # Relationships
    problem_equation = db.relationship(
        'ProblemEquationModel', backref='problem', lazy=True)

    def __init__(self, **kwargs):
        super(ProblemModel, self).__init__(**kwargs)

    def json(self):
        return {
            'id': self.id,
            'frame_id': self.frame_id,
            'description': self.description,
            'explanation': self.explanation,
            'solution': self.solution,
            'visible': self.visible,
        }

    def update(self, **kwargs):
        for key in kwargs.keys():
            setattr(self, key, kwargs[key])

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
