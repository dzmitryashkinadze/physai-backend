from app.database import db
from sqlalchemy.sql import func


class ConceptModel(db.Model):
    __tablename__ = "concept"

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    frame_id = db.Column(db.Integer, db.ForeignKey('frame.id'),
                         nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'),
                          nullable=False)
    text = db.Column(db.Text,
                     nullable=False)
    time_created = db.Column(db.DateTime(timezone=False),
                             server_default=func.now(),
                             nullable=False)
    time_updated = db.Column(db.DateTime(timezone=False),
                             onupdate=func.now())

    def __init__(self, **kwargs):
        super(ConceptModel, self).__init__(**kwargs)

    def json(self):
        return {
            'id': self.id,
            'frame_id': self.frame_id,
            'course_id': self.course_id,
            'text': self.text
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
