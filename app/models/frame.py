from app.database import db
from sqlalchemy.sql import func


class FrameModel(db.Model):
    __tablename__ = "frame"

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'),
                          nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'),
                          nullable=False)
    sequence_id = db.Column(db.Integer,
                            nullable=False)
    visible = db.Column(db.Boolean, default=False,
                        nullable=False)
    time_created = db.Column(db.DateTime(timezone=False),
                             server_default=func.now(),
                             nullable=False)
    time_updated = db.Column(db.DateTime(timezone=False),
                             onupdate=func.now())

    # Relationships
    user_actives = db.relationship(
        'UserActiveModel', backref='frame', lazy=True)
    concept = db.relationship(
        'ConceptModel', backref='frame', lazy=True, uselist=False)
    test = db.relationship(
        'TestModel', backref='frame', lazy=True, uselist=False)
    problem = db.relationship(
        'ProblemModel', backref='frame', lazy=True, uselist=False)

    def __init__(self, **kwargs):
        super(FrameModel, self).__init__(**kwargs)

    def json(self):
        return {
            'id': self.id,
            'lesson_id': self.lesson_id,
            'course_id': self.course_id,
            'sequence_id': self.sequence_id,
            'visible': self.visible
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
