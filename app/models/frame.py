from app.database import db
from sqlalchemy.sql import func


class FrameModel(db.Model):
    __tablename__ = "frame"

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'))
    sequence_id = db.Column(db.Integer)
    time_created = db.Column(db.DateTime(timezone=False),
                             server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=False),
                             onupdate=func.now())

    # Relationships
    user_active = db.relationship(
        'UserActiveModel', backref='frame', lazy=True)
    concept = db.relationship(
        'ConceptModel', backref='frame', lazy=True)
    mcq = db.relationship(
        'MCQModel', backref='frame', lazy=True)
    problem = db.relationship(
        'ProblemModel', backref='frame', lazy=True)

    def __init__(self, **kwargs):
        super(FrameModel, self).__init__(**kwargs)

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
