# importing the pariwise function
from itertools import pairwise

def compare(my_list):
    #getting all the pairs and iterating over them
    for i, j in pairwise(my_list):
        #displaying the result
        print (i, j, " ", i==j)

#  number list
compare([1, 2, 2, 3, 4, 4, 5])
