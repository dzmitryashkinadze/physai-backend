from app.database import db

course_tag = db.Table('course_tag',
                      db.Column('tag_id', db.Integer, db.ForeignKey(
                          'tag.id'), primary_key=True),
                      db.Column('course_id', db.Integer, db.ForeignKey(
                          'course.id'), primary_key=True)
                      )

course_equation = db.Table('course_equation',
                           db.Column('equation_id', db.Integer, db.ForeignKey(
                               'equation.id'), primary_key=True),
                           db.Column('course_id', db.Integer, db.ForeignKey(
                               'course.id'), primary_key=True)
                           )

problem_equation = db.Table('problem_equation',
                            db.Column('equation_id', db.Integer, db.ForeignKey(
                                'equation.id'), primary_key=True),
                            db.Column('problem_id', db.Integer, db.ForeignKey(
                                'problem.id'), primary_key=True)
                            )
