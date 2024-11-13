from flask import Flask
from flask_restful import Api, Resource
from flask_restful_swagger import swagger

app = Flask(__name__)
api = swagger.docs(Api(app), apiVersion='0.1')

# Define security definitions
security_definitions = {
	'apiKey': {
		'type': 'apiKey',
		'name': 'api_key',
		'in': 'header'
	}
}

class SecureResource(Resource):
	@swagger.operation(
		security=[{'apiKey': []}],
		responseMessages=[{'code': 401, 'message': 'Unauthorized'}]
	)
	def get(self):
		# Access restricted resource
		return {'message': 'Access granted!'}

api.add_resource(SecureResource, '/secure')

if __name__ == '__main__':
	app.run(debug=True)
