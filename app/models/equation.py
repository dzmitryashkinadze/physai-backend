from app.database import db
from sqlalchemy.sql import func


class EquationModel(db.Model):
    """
    This DB model represents a equation.
    """

    __tablename__ = "equation"

    # atributes
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    equation = db.Column(db.String(255), nullable=False)
    graph_id = db.Column(db.Integer, db.ForeignKey("graph.id"), nullable=False)
    visible = db.Column(db.Boolean, default=False, nullable=False)
    time_created = db.Column(
        db.DateTime(timezone=False), server_default=func.now(), nullable=False
    )
    time_updated = db.Column(db.DateTime(timezone=False), onupdate=func.now())

    def __init__(self, **kwargs):
        super(EquationModel, self).__init__(**kwargs)

    def json(self):
        """Return a JSON representation of a equation."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "equation": self.equation,
            "graph_id": self.graph_id,
            "visible": self.visible,
            "time_created": str(self.time_created),
            "time_updated": str(self.time_updated),
        }

    def update(self, **kwargs):
        """Update a equation."""
        for key in kwargs.keys():
            setattr(self, key, kwargs[key])

    def save_to_db(self):
        """Save a equation to the database."""
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        """Find a equation by ID."""
        return cls.query.filter_by(id=_id).first()

    def delete_from_db(self):
        """Delete a equation from the database."""
        db.session.delete(self)
        db.session.commit()
