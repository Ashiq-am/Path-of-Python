# Python3 code to demonstrate working of
# Dictionary construction from front-rear key values
# Using zip() + dict()

# initializing list
test_list = [4, 6, 3, 10, 5, 3]

# printing original list
print("The original list : " + str(test_list))

# using zip to cut first and second half
n = len(test_list)
res = dict(zip(test_list[:n // 2], test_list[n // 2:][::-1]))

# printing result
print("The mapped dictionary : " + str(res))
