from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

# In-memory data store
user_data = {}

@app.route('/put_user/<int:user_id>', methods=['PUT'])
def put_user(user_id):
	"""
	Update user data.

	---
	parameters:
	- name: user_id
		in: path
		type: integer
		required: true
		description: The ID of the user.
	- name: data
		in: body
		required: true
		schema:
		properties:
			name:
			type: string
			description: The name of the user.
			age:
			type: integer
			description: The age of the user.
	responses:
	200:
		description: A message indicating the successful update.
	"""
	try:
		data = request.json

		# Update user data in the in-memory store
		user_data[user_id] = data

		return jsonify({'message': f'Data for user {user_id} successfully updated'}), 200
	except Exception as e:
		return jsonify({'error': f'Error updating user data: {str(e)}'}), 500

@app.route('/getdata', methods=['GET'])
def getdata():
	"""
	Get all the data.

	---
	responses:
		200:
			description: Data of the user.
	"""
	return jsonify(user_data)

if __name__ == '__main__':
	app.run(debug=True)
# abhilash gaurav
