from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from app import db
import json
from app.models.physai import GraphSolver


class ProblemModel(db.Model):
    __tablename__ = 'problems'

    # atributes
    id = db.Column(db.Integer, primary_key=True)
    bundle_id = db.Column(db.Integer, ForeignKey('bundles.id'))
    text = db.Column(db.String(2000))
    graph = db.Column(db.String(2000))
    problem_number = db.Column(db.Integer)
    access = db.Column(db.Integer)
    difficulty = db.Column(db.Integer)

    # relationship properties
    bundle = relationship('BundleModel')

    def __init__(self, bundle_id, text, graph, problem_number, access, difficulty):
        self.bundle_id = bundle_id
        self.text = text
        self.graph = graph
        self.problem_number = problem_number
        self.access = access
        self.difficulty = difficulty

    # output
    def json(self):
        return {
            'id': self.id,
            'bundle_id': self.bundle_id,
            'text': self.text,
            'graph': json.loads(self.graph),
            'problem_number': self.problem_number,
            'access': self.access,
            'difficulty': self.difficulty
        }

    # summary
    def summary(self):
        return {
            'id': self.id,
            'problem_number': self.problem_number,
            'access': self.access,
            'difficulty': self.difficulty
        }

    # update the instance of class
    def update(self, **kwargs):
        if 'bundle_id' in kwargs and kwargs['bundle_id']:
            self.bundle_id = kwargs['bundle_id']
        if 'text' in kwargs and kwargs['text']:
            self.text = kwargs['text']
        if 'graph' in kwargs and kwargs['graph']:
            self.graph = str(kwargs['graph']).\
                replace("'", '"').\
                replace('False', 'false').\
                replace('True', 'true')
        if 'problem_number' in kwargs and kwargs['problem_number']:
            self.problem_number = kwargs['problem_number']
        if 'access' in kwargs and kwargs['access']:
            self.access = kwargs['access']
        if 'difficulty' in kwargs and kwargs['difficulty']:
            self.difficulty = kwargs['difficulty']

    # finder
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    # finder
    @classmethod
    def find_by_problem_number(cls, bundle_id, problem_number):
        return cls.query.filter_by(bundle_id=bundle_id).\
            filter_by(problem_number=problem_number).first()

    def check_graph(self, graph):
        json_graph = json.loads(graph.replace("'", '"').
                                replace('False', 'false').replace('True', 'true'))
        checker = GraphSolver(JSONgraph=json_graph)
        return checker.Check()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
