from app.database import db
from sqlalchemy.sql import func


class ChapterModel(db.Model):
    __tablename__ = "chapter"

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    sequence_id = db.Column(db.Integer)
    time_created = db.Column(db.DateTime(timezone=False),
                             server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=False),
                             onupdate=func.now())

    # Relationships
    lesson = db.relationship(
        'LessonModel', backref='chapter', lazy=True)

    def __init__(self, **kwargs):
        super(ChapterModel, self).__init__(**kwargs)

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
