# decorator to route URL
from flask import app


@app.route("hello")

# binding to the function of route
def hello_world():
    return ("hello world")
