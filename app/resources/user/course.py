from flask_restful import Resource
from app.models.course import CourseModel
from flask import Response, json


class Course(Resource):
    """
    This resource is used to get a course with details by id
    """

    def get(self, id):
        """Get a course by id"""

        # Find the course by id
        course = CourseModel.find_by_id(id)
        course_json = course.json()

        # Get the chapters of the course
        chapters = course.chapters
        chapters.sort(key=lambda x: x.sequence_id)

        # Update course JSON
        course_json["chapter_count"] = len(chapters)
        course_json["test_count"] = len(course.tests)
        course_json["concept_count"] = len(course.concepts)
        course_json["problem_count"] = len(course.problems)

        # Get all lessons
        lesson_count = 0
        chapter_list = []
        for chapter in chapters:
            # Get lessons from chapter
            chapter_json = chapter.json()
            lessons = chapter.lessons
            lesson_count += len(lessons)
            chapter_json["lesson_count"] = len(lessons)

            # Sort the lessons by sequence_id and serialize them
            lessons.sort(key=lambda x: x.sequence_id)
            lesson_list = []
            for lesson in lessons:
                # Convert the lesson to JSON
                lesson_json = lesson.json()
                lesson_json["completed"] = False
                lesson_list.append(lesson_json)
            chapter_json["lessons"] = lesson_list
            chapter_list.append(chapter_json)

        # Add the list of chapters and lessons to the course JSON
        course_json["chapters"] = chapter_list
        course_json["lesson_count"] = lesson_count

        # Create a response with the course JSON
        response = Response(json.dumps(course_json))
        response.headers["Content-Range"] = 1
        return response


class CourseList(Resource):
    """
    This resource is used to get all visible for users courses
    """

    def get(self):
        """Get all courses"""

        # Get all courses and convert them to JSON
        courses = list(map(lambda x: x.json(), CourseModel.query.all()))
        response = Response(json.dumps(courses))
        response.headers["Content-Range"] = len(courses)
        return response
