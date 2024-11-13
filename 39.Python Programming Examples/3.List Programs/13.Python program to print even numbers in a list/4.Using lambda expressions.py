# Python program to print Even Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93, 11]


# we can also print even no's using lambda exp.
even_nos = list(filter(lambda x: (x % 2 == 0), list1))

print("Even numbers in the list: ", even_nos)
