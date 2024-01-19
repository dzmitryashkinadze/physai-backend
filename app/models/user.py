from app.database import db
from sqlalchemy.sql import func


class UserModel(db.Model):
    """
    This DB model represents a user
    """

    __tablename__ = "user"

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(180))
    password_hash = db.Column(db.String(180))
    role = db.Column(db.Integer, default=1)
    time_created = db.Column(db.DateTime(timezone=False), server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=False), onupdate=func.now())

    def __init__(self, **kwargs):
        super(UserModel, self).__init__(**kwargs)

    def json(self):
        """Return a JSON representation of the user"""
        return {
            "id": self.id,
            "email": self.email,
            "role": self.role,
            "time_created": str(self.time_created),
            "time_updated": str(self.time_updated),
        }

    def update(self, **kwargs):
        """Update the user"""
        for key in kwargs.keys():
            setattr(self, key, kwargs[key])

    def save_to_db(self):
        """Save the user to the database"""
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        """Find a user by email"""
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, _id):
        """Find a user by id"""
        return cls.query.filter_by(id=_id).first()

    def delete_from_db(self):
        """Delete the user from the database"""
        db.session.delete(self)
        db.session.commit()
