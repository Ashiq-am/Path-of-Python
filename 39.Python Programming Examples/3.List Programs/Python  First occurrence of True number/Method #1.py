# Python3 code to demonstrate
# finding first True value
# using next() and enumerate()

# initializing list
test_list = [ 0, 0, 5, 6, 0]

# printing original list
print ("The original list is : " + str(test_list))

# finding first True value
# using next() and enumerate()
res = next((i for i, j in enumerate(test_list) if j), None)

# printing result
print ("The values till first True value : " + str(res))
