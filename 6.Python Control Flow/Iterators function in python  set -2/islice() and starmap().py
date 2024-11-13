# Python code to demonstrate the working of
# islice() and starmap()

# importing "itertools" for iterator operations
import itertools

# initializing list
li = [2, 4, 5, 7, 8, 10, 20]

# initializing tuple list
li1 = [ (1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10 , 1) ]


# using islice() to slice the list acc. to need
# starts printing from 2nd index till 6th skipping 2
print ("The sliced list values are : ",end="")
print (list(itertools.islice(li,1, 6, 2)))

# using starmap() for selection value acc. to function
# selects min of all tuple values
print ("The values acc. to function are : ",end="")
print (list(itertools.starmap(min,li1)))
