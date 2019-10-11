from flaskr.repository import db
from flaskr.model.user import User
from werkzeug.security import check_password_hash, generate_password_hash


def create_new_user(user):
    db.session.add(user)
    db.session.commit()


def query_by_id(user_id):
    return User.query.filter_by(id=user_id).first()
