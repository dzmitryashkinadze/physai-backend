from app.database import db
from sqlalchemy.sql import func


class LessonModel(db.Model):
    __tablename__ = "lesson"

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    chapter_id = db.Column(db.Integer,
                           db.ForeignKey('chapter.id'),
                           nullable=False)
    course_id = db.Column(db.Integer,
                          db.ForeignKey('course.id'),
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
    logo_path = db.Column(db.String(255), nullable=False)

    # Relationships
    user_progress_lessons = db.relationship(
        'UserProgressLessonModel', backref='lesson', lazy=True)
    user_actives = db.relationship(
        'UserActiveModel', backref='lesson', lazy=True)
    frames = db.relationship(
        'FrameModel', backref='lesson', lazy=True)

    def __init__(self, **kwargs):
        super(LessonModel, self).__init__(**kwargs)

    def json(self):
        return {
            'id': self.id,
            'chapter_id': self.chapter_id,
            'course_id': self.course_id,
            'title': self.title,
            'description': self.description,
            'sequence_id': self.sequence_id,
            'visible': self.visible,
            'logo_path': self.logo_path,
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
