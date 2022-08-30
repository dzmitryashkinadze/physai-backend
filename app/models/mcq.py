from app.database import db
from sqlalchemy.sql import func


class MCQModel(db.Model):
    __tablename__ = "mcq"

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    frame_id = db.Column(db.Integer, db.ForeignKey('frame.id'))
    question = db.Column(db.String(255))
    explanation = db.Column(db.String(255))
    time_created = db.Column(db.DateTime(timezone=False),
                             server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=False),
                             onupdate=func.now())

    # Relationships
    mcq_choice = db.relationship(
        'MCQChoiceModel', backref='mcq', lazy=True)

    def __init__(self, **kwargs):
        super(MCQModel, self).__init__(**kwargs)

    def json(self):
        return {
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
