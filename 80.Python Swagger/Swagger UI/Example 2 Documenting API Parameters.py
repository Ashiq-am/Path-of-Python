from flask import Flask, request
from flask_restful import Resource, Api
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)


class GreetUser(Resource):
	def get(self):
		"""
		Greet a user with their name.

		---
		parameters:
		- name: name
			in: query
			type: string
			required: true
			description: The name of the user to greet.
		"""
		name = request.args.get('name')
		return {'message': f'Hello, {name}!'}


api.add_resource(GreetUser, '/greet')

if __name__ == '__main__':
	app.run(debug=True)
