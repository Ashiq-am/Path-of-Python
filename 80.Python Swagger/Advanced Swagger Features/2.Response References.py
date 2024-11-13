from flask import Flask
from flask_restful import Api, Resource, fields, marshal_with

app = Flask(__name__)
api = Api(app)

# Define a response model
response_model = {
	'success': fields.Boolean(default=True),
	'message': fields.String
}

class HelloWorld(Resource):
	@marshal_with(response_model)
	def get(self):
		return {'message': 'Hello, World!'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
	app.run(debug=True)
