from flask import Flask, request
from flask_restful import Api, Resource
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app, template_file='swagger_books.yml')

books = []


class BookResource(Resource):
	def get(self, book_id):
		book = next((b for b in books if b['id'] == book_id), None)
		if book:
			return book
		else:
			return {'message': 'Book not found'}, 404

	def put(self, book_id):
		book = next((b for b in books if b['id'] == book_id), None)
		if book:
			book['title'] = request.json.get('title', book['title'])
			book['author'] = request.json.get('author', book['author'])
			return {'message': 'Book updated successfully'}
		else:
			return {'message': 'Book not found'}, 404

	def delete(self, book_id):
		global books
		books = [b for b in books if b['id'] != book_id]
		return {'message': 'Book deleted successfully'}


class BookListResource(Resource):
	def get(self):
		return {'books': books}

	def post(self):
		new_book = {
			'id': len(books) + 1,
			'title': request.json['title'],
			'author': request.json['author']
		}
		books.append(new_book)
		return {'message': 'Book created successfully'}, 201


api.add_resource(BookListResource, '/books')
api.add_resource(BookResource, '/books/<int:book_id>')

if __name__ == '__main__':
	app.run(debug=True)
