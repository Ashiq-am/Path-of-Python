# Lambda function for basic operation (square of a number)
square = lambda x: x ** 2
print(square(5))

# Lambda with Condition (check if number is even or odd)
even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(even_odd(4))

# Lambda with List Comprehension (transform a list to its squares)
numbers = [1, 2, 3, 4]
squared_numbers = [lambda x: x ** 2 for x in numbers]  # List of lambda functions
squared_list = [func(num) for func, num in zip(squared_numbers, numbers)]
print(squared_list)

# Lambda with filter() (filter numbers greater than 2)
filtered = filter(lambda x: x > 2, numbers)
print(list(filtered))

# Lambda with map() (double each number in the list)
doubled = map(lambda x: x * 2, numbers)
print(list(doubled))

# Lambda with reduce() (find the product of a list of numbers)
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)
