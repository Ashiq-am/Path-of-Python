# Python3 code to demonstrate
# index list elements pairing
# using zip()

# initializing list
test_list = [[1, 4, 5], [4, 6, 8], [8, 3, 10]]

# printing original list
print ("The original list is : " + str(test_list))

# using zip()
# to perform index list elements pairing
res = list(zip(*test_list))

# printing result
print ("The index elements pairs list is " + str(res))
