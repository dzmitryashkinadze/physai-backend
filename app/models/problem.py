from app.database import db
from sqlalchemy.sql import func


class ProblemModel(db.Model):
    """
    This DB model represents a problem.
    """

    __tablename__ = "problem"

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)
    description = db.Column(db.Text, nullable=False)
    explanation = db.Column(db.Text, nullable=False)
    solution = db.Column(db.Text, nullable=False)
    sequence_id = db.Column(db.Integer, nullable=False)
    visible = db.Column(db.Boolean, default=False, nullable=False)
    time_created = db.Column(
        db.DateTime(timezone=False), server_default=func.now(), nullable=False
    )
    time_updated = db.Column(db.DateTime(timezone=False), onupdate=func.now())

    def __init__(self, **kwargs):
        super(ProblemModel, self).__init__(**kwargs)

    def json(self):
        """Return a JSON representation of a problem."""
        return {
            "id": self.id,
            "course_id": self.course_id,
            "description": self.description,
            "explanation": self.explanation,
            "solution": self.solution,
            "sequence_id": self.sequence_id,
            "visible": self.visible,
            "time_created": self.time_created,
            "time_updated": self.time_updated,
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
