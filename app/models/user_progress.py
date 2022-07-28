from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from app import db
import json

class UserProgressModel(db.Model):
    __tablename__ = 'user_progress'

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    bundle_id = db.Column(db.Integer, ForeignKey('bundles.id'))
    progress = db.Column(db.Integer)

    # relationship properties
    user = relationship('UserModel')
    bundle = relationship('BundleModel')

    def __init__(self, user_id, bundle_id, progress):
        self.user_id = user_id
        self.bundle_id = bundle_id
        self.progress = progress

    # output
    def json(self):
        return {
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

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
