from app import app
from app.controller import UserController

@app.route('/')
def index():
    return "Hello World"

@app.route ("/users")
def users():
    return UserController.index()

@app.route ("/users/<int:id>")
def usersDetail(id):
    print(id)
    return UserController.show(id)