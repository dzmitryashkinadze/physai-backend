from app.database import db
from sqlalchemy.sql import func


class GroupModel(db.Model):
    __tablename__ = "group"

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    time_created = db.Column(db.DateTime(timezone=False),
                             server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=False),
                             onupdate=func.now())

    # Relationships
    group_course = db.relationship(
        'GroupCourseModel', backref='group', lazy=True)

    def __init__(self, **kwargs):
        super(GroupModel, self).__init__(**kwargs)

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
