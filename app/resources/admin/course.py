from flask_restful import Resource, reqparse
from app.models.course import CourseModel
from app.models.tag import TagModel
from app.models.equation import EquationModel
from flask import Response, json
from app.decorators import auth_required


class AdminCourse(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str)
    parser.add_argument('summary', type=str)
    parser.add_argument('description', type=str)
    parser.add_argument('visible', type=bool)
    parser.add_argument('logo_path', type=str)
    parser.add_argument('group_id', type=int)
    parser.add_argument('sequence_id', type=int)
    parser.add_argument('add_tag', type=str)
    parser.add_argument('delete_tag', type=str)
    parser.add_argument('add_equation', type=str)
    parser.add_argument('delete_equation', type=str)

    native_features = [
        'title',
        'summary',
        'description',
        'visible',
        'logo_path',
        'group_id',
        'sequence_id'
    ]

    @auth_required(3)
    def get(user, self, id):
        raw = CourseModel.find_by_id(int(id))
        if raw:
            return raw.json()
        return {'message': 'raw not found'}, 404

    @auth_required(3)
    def put(user, self, id):
        data = AdminCourse.parser.parse_args()
        print(data)
        data_native = {k: v for k, v in data.items(
        ) if k in AdminCourse.native_features}
        print(data_native)
        raw = CourseModel.find_by_id(int(id))
        if raw:
            raw.update(**data_native)
            if data["add_tag"]:
                tag = TagModel.find_by_id(int(data["add_tag"]))
                raw.tags.append(tag)
            if data["delete_tag"]:
                tag = TagModel.find_by_id(int(data["delete_tag"]))
                if tag in raw.tags:
                    raw.tags.remove(tag)
            if data["add_equation"]:
                equation = EquationModel.find_by_id(int(data["add_equation"]))
                raw.equations.append(equation)
            if data["delete_equation"]:
                equation = EquationModel.find_by_id(
                    int(data["delete_equation"]))
                if equation in raw.equations:
                    raw.equations.remove(equation)
        else:
            {'message': 'raw not found'}, 404
        raw.save_to_db()
        return raw.json()

    @auth_required(3)
    def delete(user, self, id):
        raw = CourseModel.find_by_id(int(id))
        if raw:
            raw.delete_from_db()
            return {'message': 'raw deleted.'}
        return {'message': 'raw not found.'}, 404


class AdminCourseList(Resource):
    @auth_required(3)
    def get(user, self):
        data = list(map(lambda x: x.json(), CourseModel.query.order_by(
            CourseModel.sequence_id).all()))
        response = Response(json.dumps(data))
        response.headers['Content-Range'] = len(data)
        return response

    @auth_required(3)
    def post(user, self):
        data = AdminCourse.parser.parse_args()
        data = {k: v for k, v in data.items(
        ) if k in AdminCourse.native_features}
        print(data)
        try:
            if data["sequence_id"] is None:
                # check highest sequence_id and set this one highest + 1
                test = list(map(lambda x: x.json(), CourseModel.query.order_by(
                    CourseModel.sequence_id).all()))
                data["sequence_id"] = test[-1]["sequence_id"] + 1
            raw = CourseModel(**data)
            raw.save_to_db()
        except Exception:
            return {'message': 'Error with raw creation'}, 404
        return raw.json(), 201
