# Python3 code to demonstrate
# Rear element extraction from Records
# using list comprehension

# initializing list of tuples
test_list = [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]

# printing original list
print("The original list is : " + str(test_list))

# using list comprehension to get names
# Rear element extraction from Records
res = [lis[-1] for lis in test_list]

# printing result
print("List with only rear tuple element : " + str(res))
