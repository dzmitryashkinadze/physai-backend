from flask_restful import Resource
from app.models.course import CourseModel
from app.models.group import GroupModel
from flask import Response, json


class Course(Resource):
    def get(self, id):
        course = CourseModel.find_by_id(id)
        course_json = course.json()
        chapters = course.chapters
        chapters.sort(key=lambda x: x.sequence_id)
        course_json['chapter_count'] = len(chapters)
        chapter_list = []
        for chapter in chapters:
            chapter_json = chapter.json()
            lessons = chapter.lessons
            chapter_json['lesson_count'] = len(lessons)
            lessons.sort(key=lambda x: x.sequence_id)
            chapter_json['lessons'] = [lesson.json()
                                       for lesson in lessons]
            chapter_list.append(chapter_json)
        course_json['chapters'] = chapter_list
        response = Response(json.dumps(course_json))
        response.headers['Content-Range'] = 1
        return response


class CourseList(Resource):
    def get(self):
        groups = list(map(lambda x: x.json(), GroupModel.query.order_by(
            GroupModel.sequence_id).all()))
        for group in groups:
            groupModel = GroupModel.find_by_id(group["id"])
            group_courses = groupModel.courses
            group_courses.sort(key=lambda x: x.sequence_id)
            group["course_count"] = len(group_courses)
            courses_container = []
            for course in group_courses:
                courses_container.append(course.json())
            group["courses"] = courses_container
        response = Response(json.dumps(groups))
        response.headers['Content-Range'] = len(groups)
        return response
