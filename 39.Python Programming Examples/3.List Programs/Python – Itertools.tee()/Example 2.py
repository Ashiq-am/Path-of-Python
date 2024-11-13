# Python code to demonstrate the working of tee()

# importing "itertools" for iterator operations
import itertools

# using tee() to make a list of iterators

iterator1, iterator2 = itertools.tee([1, 2, 3, 4, 5, 6, 7], 2)

# printing the values of iterators
print(list(iterator1))
print(list(iterator1))
print(list(iterator2))
