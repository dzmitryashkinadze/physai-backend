from flask_restful import Resource, reqparse
from app.decorators import auth_required
from werkzeug import datastructures
from flask import Response, json
import boto3
from flask import current_app

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


# check the validity of the file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# class controlling bundle resource
class AdminImage(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'image', type=datastructures.FileStorage, location='files')

    @auth_required(3)
    def post(user, self, key):
        data = AdminImage.parser.parse_args()
        image = data['image']
        filename = image.filename

        # Set up the connection to the client
        s3 = boto3.Session(
            aws_access_key_id=current_app.config.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=current_app.config.AWS_SECRET_ACCESS_KEY
        ).resource('s3')

        # check if the file name is valid
        if allowed_file(filename):
            # Upload the s3 object
            try:
                object = s3.Object('physai-frontend', 'images/' + filename)
                object.put(Body=image)
                return {'message': 'image uploaded'}, 200
            except Exception:
                return {'message': 'error while uploading'}, 400

        else:
            return {'message': 'file name is not valid'}, 400

    @auth_required(3)
    def delete(user, self, key):

        # Set up the connection to the client
        s3 = boto3.Session(
            aws_access_key_id=current_app.config.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=current_app.config.AWS_SECRET_ACCESS_KEY
        ).resource('s3')

        # Create the reference to the bucket
        my_bucket = s3.Bucket('physai-frontend')

        # Find and delete the image
        for my_bucket_object in my_bucket.objects.filter(Prefix='images/'):
            if my_bucket_object.key[7:] == key:
                try:
                    my_bucket_object.delete()
                except Exception:
                    return {'message': 'error while deleting'}, 400
        return {'message': 'image deleted'}, 200


# class controlling bundle resource
class AdminImageList(Resource):
    @auth_required(3)
    def get(user, self):

        # Set up the connection to the client
        s3 = boto3.Session(
            aws_access_key_id=current_app.config['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=current_app.config['AWS_SECRET_ACCESS_KEY']
        ).resource('s3')

        # Create the reference to the bucket
        my_bucket = s3.Bucket('physai-images')

        # Find and return all files in image directory
        images = []
        for ind, my_bucket_object in enumerate(my_bucket.objects.all()):
            images.append({"id": ind, "key": my_bucket_object.key})

        response = Response(json.dumps(images))
        response.headers['Content-Range'] = len(images)
        return response
