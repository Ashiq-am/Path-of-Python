# Python code to demonstrate the working of
# product() and permutations()

# importing "itertools" for iterator operations
import itertools

# using product() to print the cartesian product
print ("The cartesian product of the containers is : ")
print (list(itertools.product('AB','12')))

# using permutations to compute all possible permutations
print ("All the permutations of the given container is : ")
print (list(itertools.permutations('GfG',2)))
