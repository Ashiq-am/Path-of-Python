# Python code to demonstrate the working of tee()

# importing "itertools" for iterator operations
import itertools

# using tee() to make a list of iterators

for i in itertools.tee(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 4):
    # printing the values of iterators
    print(list(i))
