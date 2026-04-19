from flask import Flask

from app.extensions import mysql
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mysql.init_app(app)

    # register blueprints
    from app.routes.auth import auth
    from app.routes.main import main

    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app
