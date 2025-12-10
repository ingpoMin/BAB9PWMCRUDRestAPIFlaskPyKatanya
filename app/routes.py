from app import app
from app.controller import UserController

@app.route('/')
def index():
    return "Hello World"

@app.route ("/users")
def users():
    return UserController.index()