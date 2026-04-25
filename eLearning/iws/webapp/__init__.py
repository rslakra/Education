from os import path

from flask import Flask

from globals import db

DB_NAME = 'eLearning.db'


def create_app(test_mode: bool = False):
    # Creating new App
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Simple Secret Key"

    if test_mode:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"

    db.init_app(app)

    # Adding routes
    from .routes import routes
    app.register_blueprint(routes, url_prefix="/")

    create_database(app, test_mode=test_mode)

    return app


def create_database(app: Flask, test_mode: bool = False):
    if test_mode:
        with app.app_context():
            db.create_all()
        return
    if not path.exists(DB_NAME):
        db.create_all(app=app)
        print("Database Created!")


class WebApp:
    """Factory wrapper used by the test suite."""

    def create_app(self, test_mode: bool = False):
        return create_app(test_mode=test_mode)
