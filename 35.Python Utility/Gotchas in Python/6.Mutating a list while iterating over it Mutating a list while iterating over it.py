# working program to print a
# list of odd numbers from 1 to 10


even = lambda x : bool(x % 2)
numbers = [n for n in range(10)]

numbers[:] = [n for n in numbers if even(n)]
print(numbers)
