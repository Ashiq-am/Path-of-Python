# Python3 code to demonstrate working of
# Subtract K from each digit
# Using str() and - operator

# initializing list
test_list = [2345, 8786, 2478, 8664, 3568, 28]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 4

res = []
for ele in test_list:
    str_ele = str(ele)

    # getting maximum of 0 or negative value using max()
    # conversion of each digit to int
    new_ele = int(''.join([str(max(0, int(el) - K)) for el in str_ele]))
    res.append(new_ele)

# printing result
print("Elements after subtracting K from each digit : " + str(res))
