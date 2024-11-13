# Python3 code to demonstrate working of
# Convert Integral list to tuple list
# using zip() + list()

# initialize list
test_list = [1, 4, 6, 8, 9]

# printing original list
print("The original list : " + str(test_list))

# Convert Integral list to tuple list
# using zip() + list()
res = list(zip(test_list))

# printing result
print("List after conversion to tuple list : " + str(res))
