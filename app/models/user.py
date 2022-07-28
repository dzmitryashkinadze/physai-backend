from app import db
from sqlalchemy.orm import relationship

class UserModel(db.Model):
    __tablename__ = 'users'

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(80))
    access = db.Column(db.Integer)
    email = db.Column(db.String(80))
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    birthdate = db.Column(db.String(80))
    country = db.Column(db.String(80))

    # relationship properties
    user_progress = relationship('UserProgressModel', back_populates='user')

    def __init__(self, password, access, email, firstname='', lastname='', birthdate='', country=''):
        self.password = password
        self.access = access
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.country = country

    def json(self):
        return {
            'id': self.id,
            'email': self.email,
            'lastname': self.lastname,
            'firstname': self.firstname,
            'birthdate': self.birthdate,
            'country': self.country,
            'access': self.access
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
