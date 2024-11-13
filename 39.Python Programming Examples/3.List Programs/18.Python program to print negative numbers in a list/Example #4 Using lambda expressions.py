# Python program to print negative Numbers in a List

# list of numbers
list1 = [-10, 21, 4, -45, -66, 93, -11]


# we can also print negative no's using lambda exp.
neg_nos = list(filter(lambda x: (x < 0), list1))

print("Negative numbers in the list: ", *neg_nos)
