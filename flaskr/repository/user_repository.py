from flaskr.repository import db
from flaskr.model.user import User
from werkzeug.security import check_password_hash, generate_password_hash


def create_new_user():
    new_user = User(id=1, username='Thien Anh', password_hash=generate_password_hash('thienanh1'))
    db.session.add(new_user)
    db.session.commit()


def query_by_id(userid):
    u = User.query.filter_by(id=userid).first()
    print(u.id, u.username)
