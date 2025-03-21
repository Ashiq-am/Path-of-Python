from flask import Flask
from flask_restful import Resource, Api
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)


class HelloWorld(Resource):
	def get(self):
		"""Returns a simple hello message."""
		return {'message': 'Hello, World!'}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
	app.run(debug=True)
