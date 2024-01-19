from app.database import db
from sqlalchemy.sql import func


class ProblemEquationModel(db.Model):
    """
    This DB model represents a problem equation.
    """

    __tablename__ = "problem_equation"

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    problem_id = db.Column(db.Integer, db.ForeignKey("problem.id"), nullable=False)
    equation_id = db.Column(db.Integer, db.ForeignKey("equation.id"), nullable=False)
    time_created = db.Column(
        db.DateTime(timezone=False), server_default=func.now(), nullable=False
    )
    time_updated = db.Column(db.DateTime(timezone=False), onupdate=func.now())

    def __init__(self, **kwargs):
        super(ProblemEquationModel, self).__init__(**kwargs)

    def json(self):
        """Return a JSON representation of a problem equation."""
        return {
            "id": self.id,
            "problem_id": self.problem_id,
            "equation_id": self.equation_id,
            "time_created": str(self.time_created),
            "time_updated": str(self.time_updated),
        }

    def update(self, **kwargs):
        """Update a problem equation."""
        for key in kwargs.keys():
            setattr(self, key, kwargs[key])

    def save_to_db(self):
        """Save a problem equation to the database."""
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        """Find a problem equation by ID."""
        return cls.query.filter_by(id=_id).first()

    def delete_from_db(self):
        """Delete a problem equation from the database."""
        db.session.delete(self)
        db.session.commit()
