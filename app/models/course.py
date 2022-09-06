from app.database import db
from sqlalchemy.sql import func


class CourseModel(db.Model):
    __tablename__ = "course"

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'),
                         nullable=False)
    title = db.Column(db.String(255),
                      nullable=False)
    summary = db.Column(db.Text,
                        nullable=False)
    description = db.Column(db.Text,
                            nullable=False)
    logo_path = db.Column(db.String(255),
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
    user_ratings = db.relationship(
        'UserRatingModel', backref='course', lazy=True)
    user_feedbacks = db.relationship(
        'UserFeedbackModel', backref='course', lazy=True)
    user_progress_courses = db.relationship(
        'UserProgressCourseModel', backref='course', lazy=True)
    user_actives = db.relationship(
        'UserActiveModel', backref='course', lazy=True)
    course_tags = db.relationship(
        'CourseTagModel', backref='course', lazy=True)
    chapters = db.relationship(
        'ChapterModel', backref='course', lazy=True)
    course_equations = db.relationship(
        'CourseEquationModel', backref='course', lazy=True)
    frames = db.relationship(
        'FrameModel', backref='course', lazy=True)
    concepts = db.relationship(
        'ConceptModel', backref='course', lazy=True)
    tests = db.relationship(
        'TestModel', backref='course', lazy=True)
    problems = db.relationship(
        'ProblemModel', backref='course', lazy=True)

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
            'sequence_id': self.sequence_id,
            'visible': self.visible,
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
