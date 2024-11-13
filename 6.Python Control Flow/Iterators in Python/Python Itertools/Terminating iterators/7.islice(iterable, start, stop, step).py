# Python code to demonstrate the working of
# islice()


import itertools

# initializing list
li = [2, 4, 5, 7, 8, 10, 20]

# using islice() to slice the list acc. to need
# starts printing from 2nd index till 6th skipping 2
print("The sliced list values are : ", end="")
print(list(itertools.islice(li, 1, 6, 2)))
