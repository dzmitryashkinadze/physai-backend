from app.database import db
from sqlalchemy.sql import func


class UserProgressProblemModel(db.Model):
    """
    This DB model represents a user's progress on a problem.
    """

    __tablename__ = "user_progress_problem"

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    problem_id = db.Column(db.Integer)
    time_created = db.Column(db.DateTime(timezone=False), server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=False), onupdate=func.now())

    def __init__(self, **kwargs):
        super(UserProgressProblemModel, self).__init__(**kwargs)

    def json(self):
        """Return a JSON representation of a user's progress on a problem."""
        return {"id": self.id, "user_id": self.user_id, "problem_id": self.lesson_id}

    def update(self, **kwargs):
        """Update a user's progress on a problem."""
        for key in kwargs.keys():
            setattr(self, key, kwargs[key])

    def save_to_db(self):
        """Save a user's progress on a problem to the database."""
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        """Find a user's progress on a problem by ID."""
        return cls.query.filter_by(id=_id).first()

    def delete_from_db(self):
        """Delete a user's progress on a problem from the database."""
        db.session.delete(self)
        db.session.commit()
