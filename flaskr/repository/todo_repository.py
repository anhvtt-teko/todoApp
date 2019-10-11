from flaskr.repository import db
from flaskr.model.todo import Todo


def query_by_id(todo_id):
    return Todo.query.filter_by(id=todo_id).first()


def query_by_owner_id(owner_id):
    return Todo.query.filter_by(owner_id=owner_id).first()


def create_todo(todo):
    db.session.add(todo)
    db.session.commit()