from flask_restful import Resource
from app.models.course import CourseModel
from flask import Response, json


class Course(Resource):
    def get(self, id):
        course = CourseModel.find_by_id(id)
        course_json = course.json()
        chapters = course.chapters
        chapters.sort(key=lambda x: x.sequence_id)
        course_json["chapter_count"] = len(chapters)
        course_json["test_count"] = len(course.tests)
        course_json["concept_count"] = len(course.concepts)
        course_json["problem_count"] = len(course.problems)
        lesson_count = 0
        chapter_list = []
        for chapter in chapters:
            chapter_json = chapter.json()
            lessons = chapter.lessons
            lesson_count += len(lessons)
            chapter_json["lesson_count"] = len(lessons)
            lessons.sort(key=lambda x: x.sequence_id)
            lesson_list = []
            for lesson in lessons:
                lesson_json = lesson.json()
                lesson_json["completed"] = False
                lesson_list.append(lesson_json)
            chapter_json["lessons"] = lesson_list
            chapter_list.append(chapter_json)
        course_json["chapters"] = chapter_list
        course_json["lesson_count"] = lesson_count
        response = Response(json.dumps(course_json))
        response.headers["Content-Range"] = 1
        return response


class CourseList(Resource):
    def get(self):
        courses = list(map(lambda x: x.json(), CourseModel.query.all()))
        response = Response(json.dumps(courses))
        response.headers["Content-Range"] = len(courses)
        return response
