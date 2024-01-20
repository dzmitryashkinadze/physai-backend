from app.database import db
from sqlalchemy.sql import func


class CourseTheoryModel(db.Model):
    """
    This DB model represents a many to many relationship of course to theory.
    """

    __tablename__ = "course_theory"

    # atributes
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)
    theory_id = db.Column(db.Integer, db.ForeignKey("theory.id"), nullable=False)
    sequence = db.Column(db.Integer, nullable=False)
    time_created = db.Column(
        db.DateTime(timezone=False), server_default=func.now(), nullable=False
    )
    time_updated = db.Column(db.DateTime(timezone=False), onupdate=func.now())

    def __init__(self, **kwargs):
        super(CourseTheoryModel, self).__init__(**kwargs)

    def json(self):
        """Return a JSON representation of a problem."""
        return {
            "id": self.id,
            "course_id": self.course_id,
            "theory_id": self.theory_id,
            "sequence": self.sequence,
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
