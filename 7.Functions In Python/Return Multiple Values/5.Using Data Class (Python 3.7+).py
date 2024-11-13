from dataclasses import dataclass


@dataclass
class Book_list:
    name: str
    perunit_cost: float
    quantity_available: int = 0

    # function to calculate total cost
    def total_cost(self) -> float:
        return self.perunit_cost * self.quantity_available


book = Book_list("Introduction to programming.", 300, 3)
x = book.total_cost()

# print the total cost
# of the book
print(x)

# print book details
print(book)

# 900
Book_list(name='Python programming.',
          perunit_cost=200,
          quantity_available=3)
