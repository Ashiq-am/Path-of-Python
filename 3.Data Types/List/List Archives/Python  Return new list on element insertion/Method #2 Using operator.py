# Python3 code to demonstrate
# returning new list on element insertion
# using * operator

# initializing list
test_list = [5, 6, 2, 3, 9]

# printing original list
print ("The original list is : " + str(test_list))

# element to add
K = 10

# using * operator
# returning new list on element insertion
res = [*test_list, K]

# printing result
print ("The newly returned added list : " + str(res))
