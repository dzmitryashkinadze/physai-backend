from app.database import db
from sqlalchemy.sql import func


class MCQModel(db.Model):
    __tablename__ = "mcq"

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey('test.id'),
                        nullable=False)
    question = db.Column(db.String(255),
                         nullable=False)
    explanation = db.Column(db.String(255),
                            nullable=False)
    time_created = db.Column(db.DateTime(timezone=False),
                             server_default=func.now(),
                             nullable=False)
    time_updated = db.Column(db.DateTime(timezone=False),
                             onupdate=func.now())

    # Relationships
    mcq_choices = db.relationship(
        'MCQChoiceModel', backref='mcq', lazy=True)

    def __init__(self, **kwargs):
        super(MCQModel, self).__init__(**kwargs)

    def json(self):
        return {
            'id': self.id,
            'test_id': self.test_id,
            'question': self.question,
            'explanation': self.explanation
        }

    def update(self, **kwargs):
        for key in kwargs.keys():
            setattr(self, key, kwargs[key])

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
