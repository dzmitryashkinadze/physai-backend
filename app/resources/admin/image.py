from flask_restful import Resource, reqparse
from app.decorators import auth_required
from werkzeug import datastructures
from flask import Response, json
import boto3
from flask import request
import base64
from flask import current_app
from codecs import encode

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


# check the validity of the file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# class controlling bundle resource
class AdminImage(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('key')
    parser.add_argument('base64')
    parser.add_argument('filename', type=str)

    def __init__(self, image_bucket):
        self.image_bucket = image_bucket

    @auth_required(3)
    def delete(user, self, key):
        # Find and delete the image
        for my_bucket_object in self.image_bucket.objects.all():
            if my_bucket_object.key == key:
                try:
                    my_bucket_object.delete()
                    return {'message': 'image deleted'}, 200
                except Exception:
                    return {'message': 'error while deleting'}, 400
        return {'message': 'image not found'}, 400


# class controlling bundle resource
class AdminImageList(Resource):
    def __init__(self, image_bucket):
        self.image_bucket = image_bucket

    @auth_required(3)
    def get(user, self):
        # Find and return all files in image directory
        images = []
        for my_bucket_object in self.image_bucket.objects.all():
            images.append({"id": my_bucket_object.key})

        response = Response(json.dumps(images))
        response.headers['Content-Range'] = len(images)
        return response

    @auth_required(3)
    def post(user, self):
        data = AdminImage.parser.parse_args()
        b64_string = data['base64'].replace(
            'data:image/jpeg;base64,', '').replace(
            'data:image/png;base64,', '').replace(
            'data:image/svg+xml;base64,', '').replace(
            'data:image/svg;base64,', '').replace(
            'data:image/xml;base64,', '').strip()
        img_data = base64.b64decode(b64_string)

        # check if the file name is valid
        if allowed_file(data.filename):
            # Upload the s3 object
            try:
                self.image_bucket.put_object(Body=img_data, Key=data.filename)
                return {'message': 'image uploaded'}, 200
            except Exception:
                return {'message': 'error while uploading'}, 400

        else:
            return {'message': 'file name is not valid'}, 400
