# Python3 code to demonstrate
# Product of Prefix in list
# using list comprehension + list slicing

# compute prod
def prod(test_list):
    res = 1
    for ele in test_list:
        res = res * ele
    return res


# initializing list
test_list = [3, 4, 1, 7, 9, 1]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + list slicing
# Product of Prefix in list
res = [prod(test_list[: i + 1]) for i in range(len(test_list))]

# print result
print("The prefix prod list is : " + str(res))
