from app.database import db
from sqlalchemy.sql import func


class CourseModel(db.Model):
    __tablename__ = "course"

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    title = db.Column(db.String(255))
    summary = db.Column(db.String(255))
    description = db.Column(db.String(255))
    logo_path = db.Column(db.String(255))
    frame_number = db.Column(db.Integer)
    concept_number = db.Column(db.Integer)
    test_number = db.Column(db.Integer)
    problem_number = db.Column(db.Integer)
    visible = db.Column(db.Boolean, default=False)
    time_created = db.Column(db.DateTime(timezone=False),
                             server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=False),
                             onupdate=func.now())

    # Relationships
    user_rating = db.relationship(
        'UserRatingModel', backref='course', lazy=True)
    user_feedback = db.relationship(
        'UserFeedbackModel', backref='course', lazy=True)
    user_progress_course = db.relationship(
        'UserProgressCourseModel', backref='course', lazy=True)
    user_active = db.relationship(
        'UserActiveModel', backref='course', lazy=True)
    course_tag = db.relationship(
        'CourseTagModel', backref='course', lazy=True)
    chapter = db.relationship(
        'ChapterModel', backref='course', lazy=True)
    course_equation = db.relationship(
        'CourseEquationModel', backref='course', lazy=True)

    def __init__(self, **kwargs):
        super(CourseModel, self).__init__(**kwargs)

    def json(self):
        return {
            'id': self.id,
            'group_id': self.group_id,
            'title': self.title,
            'summary': self.summary,
            'description': self.description,
            'logo_path': self.logo_path,
            'frame_number': self.frame_number,
            'concept_number': self.concept_number,
            'test_number': self.test_number,
            'problem_number': self.problem_number,
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
