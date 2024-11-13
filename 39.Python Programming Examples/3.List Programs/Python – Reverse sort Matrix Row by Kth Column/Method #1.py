# Python3 code to demonstrate
# Reverse sort Matrix Row by Kth Column
# using sorted() + lambda + reverse()

# Initializing list
test_list = [['Manjeet', 65], ['Akshat', 42], ['Akash', 38], ['Nikhil', 192]]

# printing original lists
print("The original list is : " + str(test_list))

# Initializing K
K = 1

# Reverse sort Matrix Row by Kth Column
# using sorted() + lambda + reverse()
res = sorted(test_list, key = lambda ele: ele[K], reverse = True)

# printing result
print ("List after performing sorting of matrix records : " + str(res))
