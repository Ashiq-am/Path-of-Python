from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class UserResource(Resource):
	def get(self, user_id):
		# Retrieve user data
		return {'message': f'Retrieve user with ID {user_id}'}

class OrderResource(Resource):
	def get(self, order_id):
		# Retrieve order data
		return {'message': f'Retrieve order with ID {order_id}'}

api.add_resource(UserResource, '/user/<int:user_id>', endpoint='user')
api.add_resource(OrderResource, '/order/<int:order_id>', endpoint='order')

if __name__ == '__main__':
	app.run(debug=True)
