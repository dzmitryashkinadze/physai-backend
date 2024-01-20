from app.database import db
from sqlalchemy.sql import func


class CourseTagModel(db.Model):
    """
    This DB model represents a many to many relationship of course to problem.
    """

    __tablename__ = "course_tag"

    # atributes
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"), nullable=False)
    time_created = db.Column(
        db.DateTime(timezone=False), server_default=func.now(), nullable=False
    )
    time_updated = db.Column(db.DateTime(timezone=False), onupdate=func.now())

    def __init__(self, **kwargs):
        super(CourseTagModel, self).__init__(**kwargs)

    def json(self):
        """Return a JSON representation of a problem."""
        return {
            "id": self.id,
            "course_id": self.course_id,
            "tag_id": self.tag_id,
            "time_created": str(self.time_created),
            "time_updated": str(self.time_updated),
        }

    def update(self, **kwargs):
        """Update a problem."""
        for key in kwargs.keys():
            setattr(self, key, kwargs[key])

    def save_to_db(self):
        """Save a problem to the database."""
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        """Find a problem by ID."""
        return cls.query.filter_by(id=_id).first()

    def delete_from_db(self):
        """Delete a problem from the database."""
        db.session.delete(self)
        db.session.commit()
