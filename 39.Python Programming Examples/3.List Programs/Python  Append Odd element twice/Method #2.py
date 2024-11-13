# Python code to create a new list from initial list
# with condition to append every odd element twice.

# Importing
from itertools import chain

# List initialization
Input = [1, 2, 3, 8, 9, 11]

# Using list comprehension and chain
Output = list(chain.from_iterable([i]
			if i % 2 == 0 else [i]*2 for i in Input))

# printing
print("Initial list is:'", Input)
print("New list is:", Output)
