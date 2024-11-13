from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)	 # using swagger tool library from flasgger in python

@app.route('/hello', methods=['GET']) # route to access the flask page
def hello():
	"""
	An example endpoint that returns a greeting.

	---
	responses:
	200:
		description: A simple greeting message.
	"""
	return "Hello, Swagger!"

if __name__ == '__main__':
	app.run(debug=True)
# route to 'http://localhost:5000/apidocs/' for the tool access
