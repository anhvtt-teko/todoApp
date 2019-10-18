from flaskr.repository import db
from flaskr.model.user import User
from werkzeug.security import check_password_hash


def create_new_user(user):
    exist = check_if_exist(user.username)
    if not exist:
        db.session.add(user)
        db.session.commit()
        return user
    else:
        raise BaseException("User already exist")


def check_if_exist(username):
    exist = bool(User.query.filter_by(username=username).first())
    return exist


def query_by_id(user_id):
    return User.query.filter_by(id=user_id).first()


def query_by_username(username):
    return User.query.filter_by(username=username).first()


def validate_user(username, password):
    if not check_if_exist(username):
        return False

    user = query_by_username(username)
    if check_password_hash(user.password_hash, password):
        return True
    else:
        return False
