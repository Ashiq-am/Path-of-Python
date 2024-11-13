# Python3 code to demonstrate working of
# Remove charcters greater than K
# Using loop + ord()

# initializing list
test_list = ["geeksforgeeks", "is", "best", "for", "geeks"]

# printing original lists
print("The original list is : " + str(test_list))

# initializing K
K = 13

res = []
for ele in test_list:
    res_str = ''
    for sub in ele:

        # check for string characters
        if (ord(sub) - 97 <= K):
            res_str += sub
    res.append(res_str)

# printing result
print("Filtered List " + str(res))
