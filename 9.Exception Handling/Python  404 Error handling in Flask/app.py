from flask import Flask, render_template

app = Flask(__name__)

# app name
@app.errorhandler(404)

# inbuilt function which takes error as parameter
def not_found(e):

# defining function
return render_template("404.html")



#Flask allows us to make a python file to define all routes and functions.
# In app.py we have defined the route to the main page (‘/’) and error handler function which is a flask function and we passed
# 404 error as a parameter.
#The above python program will return 404.html file whenever the user opens a broken link.
