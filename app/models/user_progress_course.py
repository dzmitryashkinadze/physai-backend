from app.database import db
from sqlalchemy.sql import func


class UserProgressCourseModel(db.Model):
    __tablename__ = "user_progress_course"

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
                        nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'),
                          nullable=False)
    progress = db.Column(db.Integer,
                         nullable=False)
    completed = db.Column(db.Boolean,
                          nullable=False)
    time_created = db.Column(db.DateTime(timezone=False),
                             server_default=func.now(),
                             nullable=False)
    time_updated = db.Column(db.DateTime(timezone=False),
                             onupdate=func.now())

    def __init__(self, **kwargs):
        super(UserProgressCourseModel, self).__init__(**kwargs)

    def json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'course_id': self.course_id,
            'progress': self.progress,
            'completed': self.completed,
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
