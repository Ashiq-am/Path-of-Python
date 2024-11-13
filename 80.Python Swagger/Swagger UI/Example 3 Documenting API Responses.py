from flask import Flask
from flask_restful import Resource, Api
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)


class Books(Resource):
	def get(self):
		"""
		Get a list of books.

		---
		responses:
		200:
			description: A list of books.
			schema:
			type: array
			items:
				type: object
				properties:
				title:
					type: string
				author:
					type: string
		"""
		books = [
			{'title': 'Book 1', 'author': 'Author 1'},
			{'title': 'Book 2', 'author': 'Author 2'},
		]
		return books


api.add_resource(Books, '/books')

if __name__ == '__main__':
	app.run(debug=True)
