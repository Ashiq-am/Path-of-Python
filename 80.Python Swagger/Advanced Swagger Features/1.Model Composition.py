from flask import Flask
from flask_restful import Api, Resource, fields, marshal_with

app = Flask(__name__)
api = Api(app)

# Define a model
user_model = {
	'id': fields.Integer,
	'username': fields.String,
	'email': fields.String
}

class UserResource(Resource):
	@marshal_with(user_model)
	def get(self, user_id):
		# Retrieve user data from the database
		user_data = {'id': user_id, 'username': 'Geeks', 'email': 'geeks@geeksforgeeks.org'}
		return user_data

api.add_resource(UserResource, '/user/<int:user_id>')

if __name__ == '__main__':
	app.run(debug=True)
