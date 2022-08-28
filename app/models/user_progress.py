from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from app import db
import json

class UserProgressModel(db.Model):
    __tablename__ = 'user_progress'

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    bundle_id = db.Column(db.Integer)
    progress = db.Column(db.Integer)

    def __init__(self, user_id, bundle_id, progress):
        self.user_id = user_id
        self.bundle_id = bundle_id
        self.progress = progress

    # output
    def json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'bundle_id': self.bundle_id,
            'progress': self.progress
        }

    # finder
    @classmethod
    def find_progress(cls, user_id, bundle_id):
        return cls.query.\
            filter_by(user_id=user_id).\
            filter_by(bundle_id=bundle_id).\
            first()

    # finder
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
