from app.database import db
from sqlalchemy.sql import func


class ChapterModel(db.Model):
    __tablename__ = "chapter"

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'),
                          nullable=False)
    title = db.Column(db.String(255),
                      nullable=False)
    description = db.Column(db.Text,
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
    lessons = db.relationship(
        'LessonModel', backref='chapter', lazy=True)

    def __init__(self, **kwargs):
        super(ChapterModel, self).__init__(**kwargs)

    def json(self):
        return {
            'id': self.id,
            'course_id': self.course_id,
            'title': self.title,
            'description': self.description,
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
