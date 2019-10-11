from flask import Blueprint, render_template

authBp = Blueprint('auth', __name__, url_prefix='/auth')


@authBp.route('/register', methods=('GET', 'POST'))
def register():
    return render_template('auth/register.html')

@authBp.route('login', methods=('GET','POST'))
def login():
    return render_template('auth/login.html')
