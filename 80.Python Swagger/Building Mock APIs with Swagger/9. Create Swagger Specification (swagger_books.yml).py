swagger: '2.0'
info:
	title: Book API
	description: Simple Book API with CRUD operations
	version: '1.0'

paths:
	/books:
		get:
			summary: Get all books
			responses:
				'200':
					description: A list of books
		post:
			summary: Create a new book
			parameters:
				- name: book
				in: body
				required: true
				schema:
						type: object
						properties:
							title:
								type: string
								description: The title of the book
							author:
								type: string
								description: The author of the book
			responses:
				'201':
					description: Book created successfully

	/books/{book_id}:
		parameters:
			- name: book_id
			in: path
			required: true
			type: integer
		get:
			summary: Get a specific book by ID
			responses:
				'200':
					description: Book details
				'404':
					description: Book not found
		put:
			summary: Update a specific book by ID
			parameters:
				- name: book
				in: body
				required: true
				schema:
						type: object
						properties:
							title:
								type: string
								description: The updated title
							author:
								type: string
								description: The updated author
			responses:
				'200':
					description: Book updated successfully
				'404':
					description: Book not found
		delete:
			summary: Delete a specific book by ID
			responses:
				'200':
					description: Book deleted successfully
				'404':
					description: Book not found
