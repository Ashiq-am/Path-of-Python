class Author:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = Author(author)

    def display(self):
        print(f"Book: {self.title}, Author: {self.author.name}")

# Example usage:
book = Book("Python Programming", "John Doe")
book.display()
