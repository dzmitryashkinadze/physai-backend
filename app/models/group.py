from app.database import db
from sqlalchemy.sql import func


class GroupModel(db.Model):
    __tablename__ = "group"

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255),
                      nullable=False)
    description = db.Column(db.String(255),
                            nullable=False)
    sequence_id = db.Column(db.Integer,
                            nullable=False)
    visible = db.Column(db.Boolean, default=False,
                        nullable=False)
    time_created = db.Column(db.DateTime(timezone=False),
                             server_default=func.now(),
                             nullable=False)
    time_updated = db.Column(db.DateTime(timezone=False),
                             onupdate=func.now())

    # Relationships
    courses = db.relationship(
        'CourseModel', backref='group', lazy=True)

    def __init__(self, **kwargs):
        super(GroupModel, self).__init__(**kwargs)

    def json(self):
        return {
            'id': self.id,
            "title": self.title,
            "description": self.description,
            "sequence_id": self.sequence_id,
            "visible": self.visible,
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
