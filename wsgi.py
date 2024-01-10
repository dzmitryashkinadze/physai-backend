from app import create_app
from config import DevelopmentConfig

# create app from the factory
app = create_app(config_class=DevelopmentConfig)

# run the app
if __name__ == "__main__":
    app.run()
