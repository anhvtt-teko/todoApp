from flask import Flask, render_template
import os
import os

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.db'),
        SECRET_KEY=os.environ.get("SECRET_KEY", ""),
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # create the instance folder
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return render_template('index.html')

    # register auth blueprints
    from flaskr.auth import auth
    app.register_blueprint(auth.authBp)

    # create database
    from . import repository
    repository.init_app(app)

    return app
