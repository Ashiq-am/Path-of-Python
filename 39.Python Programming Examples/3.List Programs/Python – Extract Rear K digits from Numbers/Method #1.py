# Python3 code to demonstrate working of
# Extract Rear K digits from Numbers
# Using list comprehension + % operator

# initializing list
test_list = [5645, 23567, 34543, 87652, 2342]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 3

# Getting remainder for each element
res = [ele % (10 ** K) for ele in test_list]

# printing result
print("Rear K digits of elements ? : " + str(res))
