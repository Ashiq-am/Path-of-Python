# Python3 code to demonstrate working of
# List of tuples to String
# using map() + join()

# initialize list
test_list = [(1, 4), (5, 6), (8, 9), (3, 6)]

# printing original list
print("The original list is : " + str(test_list))

# List of tuples to String
# using map() + join()
res = ", ".join(map(str, test_list))

# printing result
print("Resultant string from list of tuple : " + res)
