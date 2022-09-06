from app.database import db
from sqlalchemy.sql import func


class UserActiveModel(db.Model):
    __tablename__ = "user_active"

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
                        nullable=False)
    frame_id = db.Column(db.Integer, db.ForeignKey('frame.id'),
                         nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'),
                          nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'),
                          nullable=False)
    time_created = db.Column(db.DateTime(timezone=False),
                             server_default=func.now(),
                             nullable=False)
    time_updated = db.Column(db.DateTime(timezone=False),
                             onupdate=func.now())

    def __init__(self, **kwargs):
        super(UserActiveModel, self).__init__(**kwargs)

    def json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'frame_id': self.frame_id,
            'lesson_id': self.lesson_id,
            'course_id': self.course_id,
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
