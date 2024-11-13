# Python code to demonstrate the working of
# zip_longest()

# importing "itertools" for iterator operations
import itertools

# using zip_longest() to combine two iterables.
print ("The combined values of iterables is : ")
print (*(itertools.zip_longest('GesoGes','ekfrek',fillvalue='_' )))
