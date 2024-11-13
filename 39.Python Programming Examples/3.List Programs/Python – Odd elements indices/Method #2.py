# Python3 code to demonstrate working of
# Odd elements indices
# using list comprehension

# initialize list
test_list = [5, 6, 10, 4, 7, 1, 19]

# printing original list
print("The original list is : " + str(test_list))

# Odd elements indices
# using list comprehension
res = [idx for idx, ele in enumerate(test_list) if ele % 2 != 0]

# printing result
print("Indices list Odd elements is : " + str(res))
