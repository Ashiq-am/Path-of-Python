# Python3 code to demonstrate working of
# Common list elements and dictionary values
# Using map() + slicing + lambda

# initializing list
test_list = ["Geeksforgeeks", "Best", "Geeks"]

# printing original list
print("The original list : " + str(test_list))

# initializing range
i, j = 1, 3

# map used to extend logic to each string
res = list(map(lambda x : x[i : j + 1], test_list))

# printing result
print("Sliced strings : " + str(res))
