# We import the Flask Class, an instance of
# this class will be our WSGI application.
from flask import Flask

# We create an instance of this class. The first
# argument is the name of the application’s module
# or package. __name__ is a convenient shortcut for
# this that is appropriate for most cases.This is
# needed so that Flask knows where to look for resources
# such as templates and static files.
app = Flask(__name__)


# We use the route() decorator to tell Flask what URL
# should trigger our function.
@app.route('/')
def cricgfg():
    return "Welcome to CricGFG!"


# main driver function
if __name__ == "__main__":
    # run() method of Flask class runs the
    # application on the local development server.
    app.run(debug=True)
