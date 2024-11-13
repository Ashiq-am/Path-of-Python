# Python3 code to demonstrate working of
# Subtract K from each digit
# Using list comprehension

# initializing list
test_list = [2345, 8786, 2478, 8664, 3568, 28]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 4

# list comprehension providing shorthand
res = [int(''.join([str(max(0, int(el) - K)) for el in str(ele)]))
       for ele in test_list]

# printing result
print("Elements after subtracting K from each digit : " + str(res))
