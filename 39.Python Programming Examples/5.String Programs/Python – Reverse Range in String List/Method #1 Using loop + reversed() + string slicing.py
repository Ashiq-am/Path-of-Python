# Python3 code to demonstrate working of
# Common list elements and dictionary values
# Using set() and intersection()

# initializing list
test_list = ["Geeksforgeeks", "Best", "Geeks"]

# printing original list
print("The original list : " + str(test_list))

# initializing range
i, j = 1, 3

res = []
for ele in test_list:
    # slicing and appending range
    res.append(ele[i: j + 1])

# printing result
print("Sliced strings : " + str(res))
