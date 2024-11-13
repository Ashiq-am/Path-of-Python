import json

# Sample nested JSON data
book_data = '{"title": "The Python Guide", "author": {"name": "Jane Doe", "age": 40}}'
book = json.loads(book_data)

# Nested JSON filtering
author_age = book["author"]["age"]
print(f"The author's age is {author_age}")
