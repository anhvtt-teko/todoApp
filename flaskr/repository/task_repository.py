from flaskr.repository import db
from flaskr.model.task import Task


def query_by_id(task_id):
    return Task.query.filter_by(id=task_id).first()


def query_by_owner_id(owner_id):
    return Task.query.filter_by(owner=owner_id).first()


def create_task(task):
    db.session.add(task)
    db.session.commit()


def check_if_exist(task_id):
    return bool(Task.query.filter_by(id=task_id).first())


def delete(task):
    db.session.delete(task)
    db.session.commit()


def generate_id():
    id = 0
    todo = query_by_id(id)
    while todo is not None:
        id = id + 1
        todo = query_by_id(id)
    return id


def update(task):
    old_task = query_by_id(task.id)
    old_task = task
    db.session.commit()


def check_owner(task_id, user_id):
    task = query_by_id(task_id)
    if task.owner == user_id:
        return True
    else:
        return False
