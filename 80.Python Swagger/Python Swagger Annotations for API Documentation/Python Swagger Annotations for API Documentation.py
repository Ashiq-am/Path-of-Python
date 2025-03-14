from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_swagger import swagger

app = Flask(__name__)
api = Api(app)

books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"}
]

class Book(Resource):
    def get(self, book_id):
        """
        Get a book by ID
        ---
        tags:
          - books
        parameters:
          - name: book_id
            in: path
            type: integer
            required: true
            description: The ID of the book to retrieve
        responses:
          200:
            description: A single book
            schema:
              type: object
              properties:
                id:
                  type: integer
                title:
                  type: string
                author:
                  type: string
          404:
            description: Book not found
        """
        book = next((book for book in books if book["id"] == book_id), None)
        if book:
            return jsonify(book)
        return {"message": "Book not found"}, 404

    def post(self):
        """
        Add a new book
        ---
        tags:
          - books
        parameters:
          - name: body
            in: body
            required: true
            description: The book to create
            schema:
              type: object
              properties:
                id:
                  type: integer
                title:
                  type: string
                author:
                  type: string
        responses:
          201:
            description: Book created
        """
        new_book = request.get_json()
        books.append(new_book)
        return new_book, 201

api.add_resource(Book, "/book/<int:book_id>")

@app.route("/spec")
def spec():
    return jsonify(swagger(app))

if __name__ == "__main__":
    app.run(debug=True)
