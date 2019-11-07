from flask import request
from flask_restful import Resource
from flaskr.model.user import User
from flaskr.repository import user_repository
from werkzeug.security import check_password_hash, generate_password_hash


class Auth(Resource):
    def post(self, username):
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        fullname = request.form['fullname']
        if user_repository.check_if_exist(username):
            return {"response": "User already exist"}, 400
        user = User(username=username, password_hash=hashed_password, fullname=fullname)
        user_repository.create_new_user(user)
        return {"response": "ok",
                "username": username,
                "password": password,
                "fullname": fullname}, 201


class Login(Resource):
    def post(self, username):
        password = request.form['password']
        if not user_repository.check_if_exist(username):
            return {"response": "user is not exist"}, 404
        user = user_repository.query_by_username(username)
        if not check_password_hash(user.password_hash, password):
            return {"response": "incorrect username or password"}, 400
        else:
            return {"response": "success",
                    "fullname": user.fullname}, 200


def init_app(api):
    api.add_resource(Auth, '/api/auth/<string:username>')
    api.add_resource(Login, '/api/login/<string:username>')
