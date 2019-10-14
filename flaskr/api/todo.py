from flask import request
from flask_restful import Resource
from flaskr.model.todo import Todo
from flaskr.model.user import User
from flaskr.repository import todo_repository, user_repository


class Todo(Resource):
    def get(self, todo_id):
        username = request.form['username']
        password = request.form['password']
        if not todo_repository.check_if_exist(todo_id):
            return {"response": "todo id is not exist"}, 201
        else:
            if not user_repository.validate_user(username,password):
                return {"response": "auth failed"}, 201
            todo = todo_repository.query_by_id(todo_id)
            user = user_repository.query_by_username(username)
            if todo.owner_id != user.id:
                return {"response": "wrong owner"}, 201
            else:
                return {"response": "success",
                        "title": todo.tittle,
                        "content": todo.content}, 200

    def put(self, todo_id):
        title = request.form['title']
        content = request.form['content']
        username = request.form['username']
        password = request.form['password']
        if not user_repository.validate_user(username, password):
            return {"response": "auth failed"}, 201
        user = user_repository.query_by_username(username)
        id = todo_repository.generate_id()
        todo = Todo()
        todo.id = id
        todo.tittle = title
        todo.content = content
        todo.owner_id = user.id
        todo_repository.create_todo(todo)
        return {"response": "success"}, 200


def init_app(api):
    api.add_resource(Todo, '/api/todo/<string:todo_id>')
