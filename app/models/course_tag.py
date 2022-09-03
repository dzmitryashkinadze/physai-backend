from app.database import db
from sqlalchemy.sql import func


class CourseTagModel(db.Model):
    __tablename__ = "course_tag"

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    time_created = db.Column(db.DateTime(timezone=False),
                             server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=False),
                             onupdate=func.now())

    def __init__(self, **kwargs):
        super(CourseTagModel, self).__init__(**kwargs)

    def json(self):
        return {
            'id': self.id,
            'course_id': self.course_id,
            'tag_id': self.tag_id
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
