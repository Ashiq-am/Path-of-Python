# Python code to demonstrate the working of
# combination() and combination_with_replacement()

# importing "itertools" for iterator operations
import itertools

# using combinations() to print every combination
# (without replacement)
print ("All the combination of container in sorted order(without replacement) is : ")
print (list(itertools.combinations('1234',2)))

# using combinations_with_replacement() to print every combination
# with replacement
print ("All the combination of container in sorted order(with replacement) is : ")
print (list(itertools.combinations_with_replacement('GfG',2)))
