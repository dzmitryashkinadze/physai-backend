from app import db
from sqlalchemy.orm import relationship

class BundleModel(db.Model):
    __tablename__ = "bundles"

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(80))
    level = db.Column(db.String(80))
    outline = db.Column(db.String(80))

    def __init__(self, title, level, description, outline):
        self.title = title
        self.level = level
        self.description = description
        self.outline = outline

    # full representation
    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'level': self.level,
            'outline': self.outline
        }

    # summary representation
    def summary(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'level': self.level
        }

    # update the instance of class
    def update(self, **kwargs):
        if 'title' in kwargs and kwargs['title']:
            self.title = kwargs['title']
        if 'description' in kwargs and kwargs['description']:
            self.description = kwargs['description']
        if 'level' in kwargs and kwargs['level']:
            self.level = kwargs['level']
        if 'outline' in kwargs and kwargs['outline']:
            self.outline = kwargs['outline']

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
