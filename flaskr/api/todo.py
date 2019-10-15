from flask import request
from flask_restful import Resource
from flaskr.model.user import User
from flaskr.model.task import Task
from flaskr.repository import user_repository, task_repository


class Todo(Resource):
    def get(self, todo_id):
        username = request.form['username']
        password = request.form['password']
        id = int(todo_id)
        if not task_repository.check_if_exist(id):
            return {"response": "todo id is not exist"}, 201
        else:
            if not user_repository.validate_user(username, password):
                return {"response": "auth failed"}, 201
            task = task_repository.query_by_id(id)
            user = user_repository.query_by_username(username)
            if task.owner != user.id:
                return {"response": "wrong owner"}, 201
            else:
                return {"response": "success",
                        "title": task.title,
                        "content": task.content}, 200

    def post(self, todo_id):
        title = request.form['title']
        content = request.form['content']
        username = request.form['username']
        password = request.form['password']
        if not user_repository.validate_user(username, password):
            return {"response": "auth failed"}, 201
        user = user_repository.query_by_username(username)
        id = task_repository.generate_id()
        task = Task(id=id, title=title, content=content, owner=user.id)
        task_repository.create_task(task)
        return {"response": "success"}, 200

    def put(self, todo_id):
        title = request.form['title']
        content = request.form['content']
        username = request.form['username']
        password = request.form['password']
        if not user_repository.validate_user(username, password):
            return {"response": "auth failed"}, 201
        user = user_repository.query_by_username(username)
        task = task_repository.query_by_id(todo_id)
        if task.owner != user.id:
            return {"response": "wrong owner"}, 201
        else:
            task.title = title
            task.content = content
            task_repository.update(task)
            return {"response": "success"}, 200

    def delete(self, todo_id):
        username = request.form['username']
        password = request.form['password']
        if not user_repository.validate_user(username, password):
            return {"response": "auth failed"}, 201
        user = user_repository.query_by_username(username)
        task = task_repository.query_by_id(todo_id)
        if task.owner != user.id:
            return {"response": "wrong owner"}, 201
        else:
            task_repository.delete(task)
            return {"response": "success"}, 200


def init_app(api):
    api.add_resource(Todo, '/api/todo/<string:todo_id>')
