from flaskr.repository import db
from flaskr.model.todo import Todo


def query_by_id(todo_id):
    return Todo.query.filter_by(id=todo_id).first()


def query_by_owner_id(owner_id):
    return Todo.query.filter_by(owner_id=owner_id).first()


def create_todo(todo):
    db.session.add(todo)
    db.session.commit()


def check_if_exist(todo_id):
    return bool(Todo.query.filter_by(id=todo_id).first())


def delete(todo):
    db.session.delete(todo)
    db.session.commit()


def generate_id():
    id = 0
    todo = query_by_id(id)
    while todo is not None:
        id = id + 1
        todo = query_by_id(id)
    return id
