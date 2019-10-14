from flask import request
from flask_restful import Resource
from flaskr.model.user import User
from flaskr.repository import user_repository


class Auth(Resource):
    def put(self, username):
        password = request.form['password']
        fullname = request.form['fullname']
        id = user_repository.generate_id()
        print(str(id) + " " + username)
        user = User(id=id, username=username, password_hash=password, fullname=fullname)
        success = user_repository.create_new_user(user)
        if success:
            return {"response": "ok",
                    "username": username,
                    "password": password,
                    "fullname": fullname}, 200
        else:
            return {"response": "user already exist"}, 201

    def get(self, username):
        password = request.form['password']
        if not user_repository.check_if_exist(username):
            return {"response": "user is not exist"}, 201
        user = user_repository.query_by_username(username)
        if user.password_hash != password:
            return {"response": "incorrect username or password"}, 201
        else:
            return {"response": "success",
                    "fullname": user.fullname}, 200


def init_app(api):
    api.add_resource(Auth, '/api/auth/<string:username>')
