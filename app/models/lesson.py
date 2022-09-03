from app.database import db
from sqlalchemy.sql import func


class LessonModel(db.Model):
    __tablename__ = "lesson"

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapter.id'))
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    sequence_id = db.Column(db.Integer)
    visible = db.Column(db.Boolean, default=False)
    time_created = db.Column(db.DateTime(timezone=False),
                             server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=False),
                             onupdate=func.now())

    # Relationships
    user_progress_lesson = db.relationship(
        'UserProgressLessonModel', backref='lesson', lazy=True)
    user_active = db.relationship(
        'UserActiveModel', backref='lesson', lazy=True)
    frame = db.relationship(
        'FrameModel', backref='lesson', lazy=True)

    def __init__(self, **kwargs):
        super(LessonModel, self).__init__(**kwargs)

    def json(self):
        return {
            'id': self.id,
            'chapter_id': self.chapter_id,
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
