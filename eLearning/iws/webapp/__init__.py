from os import path

from flask import Flask

from globals import db

DB_NAME = 'eLearning.db'


def create_app():
    # Creating new App
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Simple Secret Key"

    # Adding database to the application
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    # Adding routes
    from .routes import routes
    app.register_blueprint(routes, url_prefix="/")

    # create the database
    create_database(app)

    return app


def create_database(app: Flask):
    if not path.exists(DB_NAME):
        db.create_all(app=app)
        print("Database Created!")
