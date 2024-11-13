# Python3 code to demonstrate working of
# Append List every Nth index
# Using loop

# initializing list
test_list = [3, 7, 8, 2, 1, 5, 8, 9, 3]

# printing original list
print("The original list is : " + str(test_list))

# initializing Append list
app_list = ['G', 'F', 'G']

# initializing N
N = 3

res = []
for idx, ele in enumerate(test_list):

    # if index multiple of N
    if idx % N == 0:
        for ele_in in app_list:
            res.append(ele_in)
    res.append(ele)

# printing result
print("The appended list : " + str(res))
