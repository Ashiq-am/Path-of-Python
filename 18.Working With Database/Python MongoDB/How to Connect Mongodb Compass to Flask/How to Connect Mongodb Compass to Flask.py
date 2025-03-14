# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
from pymongo import MongoClient

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
client = MongoClient(
	'mongodb://localhost:27017/')

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
db = client['eshop-database']
collection = db['users']


@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
	documents = collection.find()
	for record in documents:
		print(record)
	return "HEllo"


# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()
