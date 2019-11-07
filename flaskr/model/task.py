from flaskr.repository import db


class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(100))
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))
