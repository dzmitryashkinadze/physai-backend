# main packages
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
import boto3

# migrations
migrate = Migrate()


# app factory
def create_app(config_class):

    # REST server
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Set up the connection to the client
    aws_session = boto3.Session(
        aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY']
    )
    # Set up the connection to the client
    s3 = aws_session.resource('s3')
    # Create the reference to the bucket
    image_bucket = s3.Bucket('physai-images')

    # init API object and add routes to it
    api = Api(app)
    from app.resources.routes import initialize_routes  # noqa: E402
    initialize_routes(api, image_bucket)

    # init DB
    from .database import db
    db.init_app(app)
    migrate.init_app(app, db)

    @app.before_first_request
    def initialize_database():
        db.create_all()

    # init CORS
    CORS(app, resources=r'/api/*', headers='Content-Type',
         expose_headers=['X-Total-Count', 'Content-Range'])

    return app
