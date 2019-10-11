from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate(db=db)


def init_app(app, **kwargs):
    db.app = app
    db.init_app(app)
    migrate.init_app(app)
    from flaskr.model.user import User
    from flaskr.model.todo import Todo
    db.create_all()
