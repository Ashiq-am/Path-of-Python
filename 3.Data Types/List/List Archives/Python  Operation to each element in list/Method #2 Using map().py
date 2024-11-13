# Python3 code to demonstrate
# operations on each list element
# using map()

# initializing list
test_list = ["Geeks", "foR", "gEEks", "IS", "bEST"]

# printing original list
print ("The original list is : " + str(test_list))

# operations on each list element
# using map()
# lowercasing each element
res = list(map(str.lower, test_list))

# printing result
print ("The lowercased list is : " + str(res))
