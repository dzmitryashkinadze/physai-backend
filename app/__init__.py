# main packages
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# set up the DB connection
db = SQLAlchemy()
migrate = Migrate()

# route list
from app.resources.routes import initialize_routes  # noqa: E402


# app factory
def create_app(config_class):

    # REST server
    app = Flask(__name__)
    app.config.from_object(config_class)

    # init DB
    db.init_app(app)
    migrate.init_app(app, db)

    # init api API
    api = Api(app)

    # init CORS
    CORS(app)

    # create all of the routes
    initialize_routes(api)

    return app
