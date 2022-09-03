from app.database import db
from sqlalchemy.sql import func


class UserModel(db.Model):
    __tablename__ = "user"

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(180))
    password_hash = db.Column(db.String(180))
    role = db.Column(db.Integer, default=1)
    time_created = db.Column(db.DateTime(timezone=False),
                             server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=False),
                             onupdate=func.now())

    # Relationships
    user_login = db.relationship('UserLoginModel', backref='user', lazy=True)
    user_detail = db.relationship('UserDetailModel', backref='user', lazy=True)
    user_rating = db.relationship('UserRatingModel', backref='user', lazy=True)
    user_progress_lesson = db.relationship(
        'UserProgressLessonModel', backref='user', lazy=True)
    user_progress_course = db.relationship(
        'UserProgressCourseModel', backref='user', lazy=True)
    user_active = db.relationship('UserActiveModel', backref='user', lazy=True)
    user_feedback = db.relationship(
        'UserFeedbackModel', backref='user', lazy=True)

    def __init__(self, **kwargs):
        super(UserModel, self).__init__(**kwargs)

    def json(self):
        return {
            'id': self.id,
            'email': self.email,
            'role': self.role
        }

    def update(self, **kwargs):
        for key in kwargs.keys():
            setattr(self, key, kwargs[key])

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
