# importing required ibrary
import itertools

# declaring a list
lst = [2, 2, 2]

# creating a list of pairs of the list
ordered_list = itertools.permutations(lst, 2)

# looping over the elements belonging to the
# pair of permutations
for i in ordered_list:
    # printing ith element
    print(i)
