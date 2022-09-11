from flask_restful import Resource
from app.models.lesson import LessonModel
from flask import Response, json


class Lesson(Resource):
    def get(self, id):
        lesson = LessonModel.find_by_id(id)
        lesson_json = lesson.json()
        frames = lesson.frames
        frames.sort(key=lambda x: x.sequence_id)
        lesson_json['frame_count'] = len(frames)
        frame_list = []
        for frame in frames:
            frame_json = frame.json()
            if frame.concept:
                frame_json['type'] = 'concept'
                frame_json['concept'] = frame.concept.json()
            if frame.test:
                frame_json['type'] = 'test'
                test_json = frame.test.json()
                test = frame.test
                if test.mcq:
                    test_json['type'] = 'mcq'
                    mcq_json = test.mcq.json()
                    mcq = test.mcq
                    mcq_json['choices'] = [choice.json()
                                           for choice in mcq.mcq_choices]
                    test_json['mcq'] = mcq_json
                frame_json['test'] = test_json
            if frame.problem:
                frame_json['type'] = 'problem'
                frame_json['problem'] = frame.problem.json()
            frame_list.append(frame_json)
        lesson_json['frames'] = frame_list
        response = Response(json.dumps(lesson_json))
        response.headers['Content-Range'] = 1
        return response
