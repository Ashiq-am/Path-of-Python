# Python3 code to demonstrate
# Values till False element
# using next() and enumerate()

# initializing list
test_list = [ 1, 5, 0, 0, 6]

# printing original list
print ("The original list is : " + str(test_list))

# Values till False element
# using next() and enumerate()
res = next((i for i, j in enumerate(test_list) if not j), None)

# printing result
print ("The values till first False value : " + str(res))
