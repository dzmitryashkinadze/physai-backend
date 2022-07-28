from app import db
import json
from app.models.physai import GraphSolver
from sqlalchemy.orm import relationship

class SkillModel(db.Model):
    __tablename__ = 'skills'

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    graph = db.Column(db.String(2000))
    equation = db.Column(db.String(80))

    def __init__(self, name, graph, front_graph, equation):
        self.name = name
        self.graph = graph
        self.equation = equation

    # output
    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'graph': json.loads(self.graph),
            'equation': self.equation
        }

    # summary
    def summary(self):
        return {
            'id': self.id,
            'name': self.name,
            'equation': self.equation
        }

    # update the instance of class
    def update(self, **kwargs):
        if 'name' in kwargs and kwargs['name']:
            self.name = kwargs['name']
        if 'graph' in kwargs and kwargs['graph']:
            self.graph = str(kwargs['graph']).replace("'", '"').replace('False', 'false').replace('True','true')
        if 'equation' in kwargs and kwargs['equation']:
            self.equation = kwargs['equation']

    # finder
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    #def generate_front_graph(self):
    #    a = GraphSolver(JSONgraph = json.loads(self.graph))
    #    front_graph = a.generate_summary_graph(self.id, self.name, self.equation)
    #    return json.loads(front_graph)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
