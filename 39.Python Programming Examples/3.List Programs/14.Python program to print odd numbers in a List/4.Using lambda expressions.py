# Python program to print odd numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93, 11]


# we can also print odd no's using lambda exp.
odd_nos = list(filter(lambda x: (x % 2 != 0), list1))

print("Odd numbers in the list: ", odd_nos)
