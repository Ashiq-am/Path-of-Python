from itertools import chain

# a list of odd numbers
odd = [1, 3, 5, 7, 9]

# a list of even numbers
even = [2, 4, 6, 8, 10]

# chaining odd and even numbers
numbers = list(chain(odd, even))

print(numbers)
