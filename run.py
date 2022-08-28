from app import create_app
from config import DevelopmentConfig

# create app from the factory
this_app = create_app(config_class=DevelopmentConfig)


# run the app
if __name__ == "__main__":
    this_app.run(port=8080)
