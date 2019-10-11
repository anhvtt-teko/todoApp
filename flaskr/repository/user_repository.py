from flaskr.repository import db
from flaskr.model.user import User


def create_new_user(user):
    exist = check_if_exist(user.username)
    if not exist:
        db.session.add(user)
        db.session.commit()
        return True
    else:
        return False


def check_if_exist(username):
    exist = bool(User.query.filter_by(username=username).first())
    return exist


def query_by_id(user_id):
    return User.query.filter_by(id=user_id).first()


def query_by_username(username):
    return User.query.filter_by(username=username).first()


def generate_id():
    id = 0
    user = query_by_id(id)
    while user is not None:
        id = id + 1
        user = query_by_id(id)
    return id
