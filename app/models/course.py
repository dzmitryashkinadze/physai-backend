from app.database import db
from sqlalchemy.sql import func


class CourseModel(db.Model):
    """
    This DB model represents a course.
    """

    __tablename__ = "course"

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    summary = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    sequence = db.Column(db.Integer, nullable=False)
    visible = db.Column(db.Boolean, default=False, nullable=False)
    time_created = db.Column(
        db.DateTime(timezone=False), server_default=func.now(), nullable=False
    )
    time_updated = db.Column(db.DateTime(timezone=False), onupdate=func.now())

    # Relationships
    problems = db.relationship("ProblemModel", backref="course", lazy=True)

    def __init__(self, **kwargs):
        super(CourseModel, self).__init__(**kwargs)

    def json(self):
        """Return a JSON representation of a course."""
        return {
            "id": self.id,
            "title": self.title,
            "summary": self.summary,
            "description": self.description,
            "sequence": self.sequence,
            "visible": self.visible,
            "time_created": str(self.time_created),
            "time_updated": str(self.time_updated),
        }

    def update(self, **kwargs):
        """Update a course."""
        for key in kwargs.keys():
            setattr(self, key, kwargs[key])

    def save_to_db(self):
        """Save a course to the database."""
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        """Find a course by ID."""
        return cls.query.filter_by(id=_id).first()

    def delete_from_db(self):
        """Delete a course from the database."""
        db.session.delete(self)
        db.session.commit()
