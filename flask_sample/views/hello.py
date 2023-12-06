from flask import Blueprint, request, url_for, redirect
hello = Blueprint('hello', __name__, url_prefix='/')


@hello.route('/')
def index():
    name = request.args.get('name', 'World')
    return redirect(url_for("auth.login"))
    #return f'Hello {name}!'