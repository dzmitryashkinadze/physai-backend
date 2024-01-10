from app.database import db
from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from config import DevelopmentConfig

app = Flask(__name__)
with app.app_context():
    app.config.from_object(DevelopmentConfig)
    migrate = Migrate()

    api = Api(app)
    from app.resources.routes import initialize_routes

    initialize_routes(api)

    db.init_app(app)
    migrate.init_app(app, db)
    db.create_all()
