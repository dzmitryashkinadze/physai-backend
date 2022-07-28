from flask_restful import Resource, reqparse
from app.decorators import auth_required
from werkzeug import datastructures
import boto3

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


# check the validity of the file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# class controlling bundle resource
class Image(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('image', type=datastructures.FileStorage, location='files')

    @auth_required(3)
    def post(user, self, key):
        data = Image.parser.parse_args()
        image = data['image']
        filename = image.filename

        # check if the file name is valid
        if allowed_file(filename):

            # Set up the connection to the client
            s3 = boto3.Session(
                aws_access_key_id='AKIASUPTJ3EL3RYCQJZ5',
                aws_secret_access_key='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'
            ).resource('s3')

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
            aws_access_key_id='AKIASUPTJ3EL3RYCQJZ5',
            aws_secret_access_key='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'
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
class ImageList(Resource):
    @auth_required(3)
    def get(user, self):

        # Set up the connection to the client
        s3 = boto3.Session(
            aws_access_key_id='AKIASUPTJ3EL3RYCQJZ5',
            aws_secret_access_key='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'
        ).resource('s3')

        # Create the reference to the bucket
        my_bucket = s3.Bucket('physai-frontend')

        # Find and return all files in image directory
        images = []
        for my_bucket_object in my_bucket.objects.filter(Prefix='images/'):
            images.append(my_bucket_object.key[7:])
        return {'images': images}, 200
