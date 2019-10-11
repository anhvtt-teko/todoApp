from flask import request
from flask_restful import Resource
from flaskr.model.user import User
from flaskr.repository.user_repository import generate_id, create_new_user


class Register(Resource):
    def put(self):
        username = request.form['username']
        password = request.form['password']
        fullname = request.form['fullname']
        id = generate_id()
        print(str(id) + " " + username)
        user = User(id=id, username=username, password_hash=password, fullname=fullname)
        success = create_new_user(user)
        if success:
            return {"response": "ok",
                    "username": username,
                    "password": password,
                    "fullname": fullname}, 200
        else:
            return {"response": "user already exist"}, 201


def init_app(api):
    api.add_resource(Register, '/api/register')
