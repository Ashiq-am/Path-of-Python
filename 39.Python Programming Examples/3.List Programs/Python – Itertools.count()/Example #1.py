# Program for creating a list of
# even and odd list of integers
# using count()


from itertools import count

# creates a count iterator object
iterator =(count(start = 0, step = 2))

# prints a odd list of integers
print("Even list:",
	list(next(iterator) for _ in range(5)))

# creates a count iterator object
iterator = (count(start = 1, step = 2))

# prints a odd list of integers
print("Odd list:",
	list(next(iterator) for _ in range(5)))
