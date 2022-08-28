from app.database import db


class UserModel(db.Model):
    __tablename__ = "user"

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(180))
    password_hash = db.Column(db.String(180))
    role = db.Column(db.Integer)
    created = db.Column(db.Date)

    def __init__(self, **kwargs):
        super(UserModel, self).__init__(**kwargs)

    def json(self):
        return {
            'email': self.email,
            'role': self.role
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
