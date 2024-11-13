# importing the required library
import pandas as p

# Defining the list
l = [12, 4, 3, 7, 8, 10, 22]

# Printing the index of the maximum element
print("Index of the max element in a list is", p.Series(l).idxmax())
