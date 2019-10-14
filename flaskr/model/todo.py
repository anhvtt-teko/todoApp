from flaskr.repository import db


class Todo(db.Model):
    __tablename__ = 'todo'

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        return '<Todo %r>' % self.username

    id = db.Column(db.String(50), primary_key=True)
    tittle = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(100))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    owner = db.relationship('User', backref=db.backref('todos', lazy=True))
