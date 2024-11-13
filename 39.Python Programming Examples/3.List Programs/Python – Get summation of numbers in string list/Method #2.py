# Python3 code to demonstrate working of
# Summation of String Integer lists
# using sum() + int() + list comprehension

# initialize list
test_list = [['1', '4'], ['5', '6'], ['7', '10']]

# printing original list
print("The original list : " + str(test_list))

# Summation of String Integer lists
# using sum() + int() + list comprehension
res = [sum(int(ele) for ele in sub) for sub in test_list]

# printing result
print("List after summation of nested string lists : " + str(res))
