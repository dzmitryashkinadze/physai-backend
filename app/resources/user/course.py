from flask_restful import Resource
from app.models.group import GroupModel
from flask import Response, json


class CourseList(Resource):
    def get(self):
        groups = list(map(lambda x: x.json(), GroupModel.query.all()))
        for group in groups:
            groupModel = GroupModel.find_by_id(group["id"])
            group_courses = groupModel.courses
            group["course_count"] = len(group_courses)
            courses_json = {}
            for ind, course in enumerate(group_courses):
                courses_json[ind] = course.json()
            group["courses"] = courses_json
        print(groups)
        response = Response(json.dumps(groups))
        response.headers['Content-Range'] = len(groups)
        return response
