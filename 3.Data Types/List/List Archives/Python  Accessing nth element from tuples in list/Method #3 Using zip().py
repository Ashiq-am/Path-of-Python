# Python code to demonstrate
# get nth tuple element from list
# using zip()

# initializing list of tuples
test_list = [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]

# printing original list
print("The original list is : " + str(test_list))

# using zip() to get names
res = list(zip(*test_list)[1])

# printing result
print("List with only nth tuple element (i.e names) : " + str(res))
