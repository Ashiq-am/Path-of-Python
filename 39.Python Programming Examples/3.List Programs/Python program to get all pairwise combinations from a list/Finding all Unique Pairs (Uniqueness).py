# importing required library
import itertools


# creating a list of elements belonging

#3 to integers and strings
lst = [1,"Mallika",2,"Yash"]

# simulating permutations of the list in
# a group of 2
pair_order_list = itertools.combinations(lst,2)

# printing the elements belonging to permutations
print (list(pair_order_list))
