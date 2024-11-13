def square(number):
    return number * number

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)

for number in squared_numbers:
    print(number)
