# With assignment expressions
squared_numbers = [y for x in range(10) if (y := x ** 2) % 2 == 0]
print(squared_numbers)
